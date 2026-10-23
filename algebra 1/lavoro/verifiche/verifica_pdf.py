"""Verifica tutti gli estratti correnti della raccolta e confronta il rendering."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

from PIL import Image, ImageChops
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[3]
VIEWS = Path('/private/tmp/algebra-verifica-finale')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def render(pdf, target):
    target.mkdir(parents=True, exist_ok=True)
    for old in target.glob('p-*.png'):
        old.unlink()
    subprocess.run(['pdftoppm', '-scale-to', '1500', '-png', str(pdf), str(target / 'p')],
                   check=True, capture_output=True)
    return sorted(target.glob('p-*.png'))


def target_page(reader, destination):
    if isinstance(destination, str):
        assert destination in reader.named_destinations, destination
        return reader.get_destination_page_number(reader.named_destinations[destination])
    page = destination[0]
    if isinstance(page, int):
        return page
    return reader.get_page_number(page.get_object())


def run():
    subjects = sys.argv[1:] or ['algebra 1', 'analisi 1', 'geometria 1']
    target = ROOT / 'strumenti/VERIFICA_ESPORTAZIONE_2026-10-23.json'
    report = (json.loads(target.read_text()) if sys.argv[1:] and target.exists()
              else {'data': '2026-10-23', 'materie': [], 'confronto': 'tutte le pagine e tutte le annotazioni'})
    report['materie'] = [item for item in report['materie'] if item['materia'] not in subjects]
    for name in subjects:
        folder = ROOT / name
        pdf = folder / 'build/main.pdf'
        volume = PdfReader(pdf)
        manifest = json.loads((folder / 'build/capitoli/manifest.json').read_text())
        assert manifest['origine_sha256'] == digest(pdf)
        main_images = render(pdf, VIEWS / name / 'volume')
        assert len(main_images) == len(volume.pages)
        checked = []
        for chapter in manifest['capitoli']:
            part_pdf = folder / 'build/capitoli' / chapter['file']
            part = PdfReader(part_pdf)
            start = chapter['pagina_pdf_iniziale'] - 1
            stop = chapter['pagina_pdf_finale']
            assert len(part.pages) == stop - start
            assert part.page_labels == volume.page_labels[start:stop]
            assert digest(part_pdf) == chapter['sha256']
            part_images = render(part_pdf, VIEWS / name / f"capitolo-{chapter['numero']:02d}")
            local, remote, others = 0, 0, 0
            for offset, (source, extracted) in enumerate(zip(volume.pages[start:stop], part.pages)):
                assert source.get_contents().get_data() == extracted.get_contents().get_data()
                assert source.extract_text() == extracted.extract_text()
                assert source.mediabox == extracted.mediabox and source.cropbox == extracted.cropbox
                with Image.open(main_images[start + offset]) as a, Image.open(part_images[offset]) as b:
                    assert a.size == b.size
                    assert ImageChops.difference(a.convert('RGB'), b.convert('RGB')).getbbox() is None
                original_annotations = source.get('/Annots', [])
                extracted_annotations = extracted.get('/Annots', [])
                assert len(original_annotations) == len(extracted_annotations)
                for a, b in zip(original_annotations, extracted_annotations):
                    a, b = a.get_object(), b.get_object()
                    assert a.get('/Rect') == b.get('/Rect')
                    assert a.get('/Subtype') == b.get('/Subtype')
                    aa, ba = a.get('/A', {}), b.get('/A', {})
                    destination = a.get('/Dest', aa.get('/D'))
                    if destination is not None and (a.get('/Dest') is not None or aa.get('/S') == '/GoTo'):
                        expected = target_page(volume, destination)
                        assert expected is not None
                        if start <= expected < stop:
                            assert ba.get('/S') == '/GoTo'
                            assert target_page(part, ba['/D']) == expected - start
                            local += 1
                        else:
                            assert ba.get('/S') == '/GoToR'
                            assert ba['/F'] == '../main.pdf'
                            assert (part_pdf.parent / ba['/F']).resolve() == pdf.resolve()
                            assert target_page(volume, ba['/D']) == expected
                            remote += 1
                    else:
                        assert aa == ba
                        others += 1
            checked.append({'numero': chapter['numero'], 'file': chapter['file'],
                            'pagine': len(part.pages), 'flussi_testo_formato_numerazione_identici': True,
                            'pixel_identici_tutte_le_pagine': True, 'link_interni': local,
                            'link_al_volume': remote, 'altre_annotazioni': others})
        log = (folder / 'build/main.log').read_text()
        warnings = [line for line in log.splitlines()
                    if any(word in line for word in ['Warning', 'Overfull', 'Underfull', 'Undefined control'])]
        assert not warnings, (name, warnings)
        report['materie'].append({'materia': name, 'pagine_volume': len(volume.pages),
                                  'volume_sha256': digest(pdf), 'avvisi_latex': warnings,
                                  'estratti': checked})
        print(name, len(volume.pages), 'pagine;', len(checked), 'estratti verificati', flush=True)
    sources = json.loads((ROOT / 'algebra 1/fonti/manifest.json').read_text())
    all_sources = sources['fonti'] + sources.get('serie_M-Z', {}).get('fonti', [])
    for source in all_sources:
        saved = ROOT / 'algebra 1' / source['file']
        assert digest(saved) == source['sha256']
        assert saved.read_bytes() == Path(source['origine']).read_bytes()
    report['fonti_algebra'] = {'pdf_identici_agli_originali': len(all_sources),
                              'serie_primaria': 'A–L', 'serie_supporto': 'M–Z',
                              'pagine_inventariate': sources['totale_pagine']}
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    run()
