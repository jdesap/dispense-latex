#!/usr/bin/env python3
"""Estrae i capitoli numerati dal PDF completo dopo una build riuscita."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unicodedata


def load_pdf_library():
    try:
        from pypdf import PdfReader, PdfWriter
        return PdfReader, PdfWriter
    except ModuleNotFoundError as error:
        if error.name != "pypdf":
            raise
        # Python di sistema resta il punto di ingresso. Su questo Mac si
        # riutilizza il runtime già fornito da Codex, senza installazioni.
        bundled = (Path.home() / ".cache/codex-runtimes/codex-primary-runtime"
                   / "dependencies/python/bin/python3")
        if bundled.is_file() and bundled.resolve() != Path(sys.executable).resolve():
            probe = subprocess.run(
                [str(bundled), "-c", "import pypdf"],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            )
            if probe.returncode == 0:
                os.execv(str(bundled), [str(bundled), str(Path(__file__).resolve()),
                                       *sys.argv[1:]])
        raise RuntimeError(
            "Manca la libreria pypdf. Usare un Python con pypdf tramite "
            "DISPENSE_PYTHON, oppure installarla nell'ambiente Python scelto."
        ) from error


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def slug(text):
    plain = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", plain.lower()).strip("-") or "capitolo"


def numbered_chapters(reader):
    chapters = []
    # Gli elementi annidati sono sezioni e sottosezioni, non capitoli.
    for item in reader.outline:
        if isinstance(item, list):
            continue
        match = re.fullmatch(r"(\d+)\s+(.+)", item.title)
        if not match:
            continue
        start = reader.get_destination_page_number(item)
        if start is None or start < 0:
            raise ValueError(f"Destinazione non valida: {item.title}")
        number, title = int(match[1]), match[2].strip()
        chapters.append({"numero": number, "titolo": title, "inizio": start,
                         "file": f"{number:02d}-{slug(title)}.pdf"})
    if not chapters:
        raise ValueError("Nessun capitolo numerato nei segnalibri del PDF.")
    for index, chapter in enumerate(chapters):
        stop = chapters[index + 1]["inizio"] if index + 1 < len(chapters) else len(reader.pages)
        if stop <= chapter["inizio"]:
            raise ValueError("I capitoli devono iniziare su pagine distinte e ordinate.")
        chapter["fine"] = stop
    if len({c["file"] for c in chapters}) != len(chapters):
        raise ValueError("Nomi dei capitoli duplicati.")
    return chapters


def set_page_labels(writer, labels):
    # Le etichette seguono i numeri stampati nel main, anche se l'estratto
    # inizia fisicamente dalla propria prima pagina.
    if labels and all(label.isdecimal() for label in labels):
        first = int(labels[0])
        if labels == [str(first + i) for i in range(len(labels))]:
            writer.set_page_label(0, len(labels) - 1, style="/D", start=first)
            return
    for index, label in enumerate(labels):
        writer.set_page_label(index, index, prefix=label)


def copy_annotations(reader, writer, start, stop, volume_name):
    """Conserva i link interni e rende remoti quelli fuori dall'estratto.

    Le annotazioni vengono ricopiate esplicitamente: append filtrerebbe
    quelle dirette a pagine escluse e alcune versioni segnalano inoltre
    differenze attese fra le due liste di link durante tale filtraggio.
    Nessuna pagina del volume o copia annotata viene modificata.
    """
    from pypdf.generic import (
        ArrayObject, DictionaryObject, NameObject, NumberObject,
        TextStringObject,
    )

    page_numbers = {page.indirect_reference.idnum: index
                    for index, page in enumerate(reader.pages)}
    for offset, source in enumerate(reader.pages[start:stop]):
        annotations = ArrayObject()
        for reference in source.get("/Annots", []):
            original = reference.get_object()
            copied = original.clone(writer, ignore_fields=("/P", "/Dest", "/A"))
            action = original.get("/A")
            if action is not None:
                action = action.get_object()
            destination = original.get("/Dest")
            if action is not None and action.get("/S") == "/GoTo":
                destination = action.get("/D")
            if destination is None:
                if action is not None:
                    copied[NameObject("/A")] = action.clone(writer)
            else:
                destination = destination.get_object()
                if isinstance(destination, str):
                    target = reader.named_destinations.get(str(destination))
                    if target is None:
                        raise ValueError(f"Destinazione inesistente: {destination}")
                    page_number = reader.get_destination_page_number(target)
                    local_destination = TextStringObject(str(destination))
                    remote_destination = TextStringObject(str(destination))
                else:
                    page_number = page_numbers.get(destination[0].idnum)
                    if page_number is None:
                        raise ValueError("Link a una pagina estranea al volume.")
                    tail = [value.clone(writer) for value in destination[1:]]
                    remote_destination = ArrayObject([NumberObject(page_number), *tail])
                    local_destination = (ArrayObject([
                        writer.pages[page_number - start].indirect_reference, *tail,
                    ]) if start <= page_number < stop else None)
                if page_number is None or page_number < 0:
                    raise ValueError("Destinazione senza pagina valida.")
                if start <= page_number < stop:
                    copied[NameObject("/A")] = DictionaryObject({
                        NameObject("/S"): NameObject("/GoTo"),
                        NameObject("/D"): local_destination,
                    })
                else:
                    copied[NameObject("/A")] = DictionaryObject({
                        NameObject("/S"): NameObject("/GoToR"),
                        NameObject("/F"): TextStringObject(f"../{volume_name}"),
                        NameObject("/D"): remote_destination,
                    })
            annotations.append(writer._add_object(copied))
        if annotations:
            writer.pages[offset][NameObject("/Annots")] = annotations


def export(pdf):
    PdfReader, PdfWriter = load_pdf_library()
    from pypdf.generic import NameObject
    pdf = pdf.resolve(strict=True)
    reader = PdfReader(pdf)
    chapters = numbered_chapters(reader)
    labels = reader.page_labels
    output = pdf.parent / "capitoli"
    output.mkdir(exist_ok=True)
    manifest_path = output / "manifest.json"
    previous = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    previous_files = {c["file"] for c in previous.get("capitoli", [])}
    exported = []

    # Si preparano tutti i PDF prima di sostituire quelli correnti.
    with tempfile.TemporaryDirectory(prefix=".esportazione-", dir=output) as temp:
        stage = Path(temp)
        for chapter in chapters:
            start, stop = chapter["inizio"], chapter["fine"]
            writer = PdfWriter()
            # Evita anche il tentativo di abbinare link durante la copia:
            # le annotazioni sono ripristinate in memoria prima di ricopiarle.
            # Il PDF sorgente su disco non viene mai modificato.
            saved_annotations = [(page, page.pop(NameObject("/Annots"), None))
                                 for page in reader.pages[start:stop]]
            try:
                writer.append(reader, pages=(start, stop), import_outline=True,
                              excluded_fields=("/Annots",))
            finally:
                for page, annotations in saved_annotations:
                    if annotations is not None:
                        page[NameObject("/Annots")] = annotations
            copy_annotations(reader, writer, start, stop, pdf.name)
            metadata = reader.metadata or {}
            writer.add_metadata({
                "/Title": f"{metadata.get('/Title', pdf.stem)} - {chapter['titolo']}",
                "/Author": str(metadata.get("/Author", "")),
                "/Subject": f"Capitolo {chapter['numero']}: {chapter['titolo']}",
            })
            set_page_labels(writer, labels[start:stop])
            target = stage / chapter["file"]
            with target.open("wb") as stream:
                writer.write(stream)
            check = PdfReader(target)
            if len(check.pages) != stop - start:
                raise ValueError(f"Numero di pagine errato: {chapter['file']}")
            if check.page_labels != labels[start:stop]:
                raise ValueError(f"Numerazione errata: {chapter['file']}")
            exported.append({
                "numero": chapter["numero"], "titolo": chapter["titolo"],
                "file": chapter["file"], "pagine": stop - start,
                "pagina_pdf_iniziale": start + 1, "pagina_pdf_finale": stop,
                "numero_stampato_iniziale": labels[start],
                "numero_stampato_finale": labels[stop - 1],
                "sha256": digest(target),
            })
        current_files = {c["file"] for c in exported}
        for name in sorted(previous_files - current_files):
            # Un capitolo rinominato non resta fra gli estratti correnti.
            # Si sposta soltanto un file precedentemente generato qui.
            if Path(name).name != name or not name.endswith(".pdf"):
                raise ValueError("Nome non valido nel precedente manifest.")
            old = output / name
            if old.is_file():
                archive = output / "precedenti"
                archive.mkdir(exist_ok=True)
                saved = archive / f"{old.stem}-{digest(old)[:12]}.pdf"
                os.replace(old, saved)
        for item in exported:
            target = output / item["file"]
            if not target.exists() or digest(target) != item["sha256"]:
                os.replace(stage / item["file"], target)
        manifest = {
            "origine": pdf.name, "origine_sha256": digest(pdf),
            "pagine_volume": len(reader.pages),
            "criterio": "capitoli numerati nei segnalibri; pagine e impaginazione del volume",
            "capitoli": exported,
        }
        staged_manifest = stage / "manifest.json"
        staged_manifest.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
        os.replace(staged_manifest, manifest_path)
    print(f"Estratti {len(exported)} capitoli in {output}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", required=True, type=Path)
    args = parser.parse_args()
    try:
        export(args.pdf)
    except Exception as error:
        print(f"Esportazione capitoli: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
