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


def export(pdf):
    PdfReader, PdfWriter = load_pdf_library()
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
            writer.append(reader, pages=(start, stop), import_outline=True)
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
