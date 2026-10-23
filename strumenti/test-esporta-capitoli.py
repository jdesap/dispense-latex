"""Regressione dei link degli estratti: nomi, coordinate, URI e pagine escluse."""
import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest

from pypdf import PdfReader, PdfWriter
from pypdf.generic import (
    ArrayObject, DictionaryObject, FloatObject, NameObject, TextStringObject,
)

sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location('exporter', Path(__file__).with_name('esporta-capitoli.py'))
exporter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(exporter)


class ChapterLinks(unittest.TestCase):
    def test_preserves_named_direct_remote_and_uri_links(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / 'main.pdf'
            writer = PdfWriter()
            for _ in range(4):
                writer.add_blank_page(width=595, height=842)
            writer.add_outline_item('1 Primo', 0)
            writer.add_outline_item('2 Secondo', 2)
            writer.add_named_destination('primo', 1)
            writer.add_named_destination('secondo', 3)
            writer.set_page_label(0, 3, style='/D', start=7)

            def link(destination=None, uri=None):
                action = DictionaryObject({NameObject('/S'): NameObject('/GoTo' if uri is None else '/URI')})
                action[NameObject('/D' if uri is None else '/URI')] = destination if uri is None else TextStringObject(uri)
                return DictionaryObject({
                    NameObject('/Type'): NameObject('/Annot'), NameObject('/Subtype'): NameObject('/Link'),
                    NameObject('/Rect'): ArrayObject([FloatObject(x) for x in (10, 20, 30, 40)]),
                    NameObject('/A'): action,
                })

            direct_local = ArrayObject([writer.pages[1].indirect_reference, NameObject('/XYZ'),
                                        FloatObject(12), FloatObject(34), FloatObject(1)])
            direct_remote = ArrayObject([writer.pages[3].indirect_reference, NameObject('/FitH'), FloatObject(56)])
            for annotation in [link(TextStringObject('primo')), link(TextStringObject('secondo')),
                               link(direct_local), link(direct_remote), link(uri='https://example.org/')]:
                writer.add_annotation(0, annotation)
            writer.write(source)
            before = source.read_bytes()
            exporter.export(source)
            self.assertEqual(before, source.read_bytes())
            part = PdfReader(Path(tmp) / 'capitoli/01-primo.pdf')
            self.assertEqual(part.page_labels, ['7', '8'])
            actions = [x.get_object()['/A'] for x in part.pages[0]['/Annots']]
            self.assertEqual(len(actions), 5)
            self.assertEqual(actions[0]['/S'], '/GoTo')
            self.assertEqual(part.get_destination_page_number(part.named_destinations['primo']), 1)
            self.assertEqual(actions[1]['/S'], '/GoToR')
            self.assertEqual(actions[1]['/F'], '../main.pdf')
            self.assertEqual(actions[1]['/D'], 'secondo')
            self.assertEqual(part.get_page_number(actions[2]['/D'][0].get_object()), 1)
            self.assertEqual(list(actions[2]['/D'][1:]), ['/XYZ', 12, 34, 1])
            self.assertEqual(actions[3]['/S'], '/GoToR')
            self.assertEqual(list(actions[3]['/D']), [3, '/FitH', 56])
            self.assertEqual(actions[4]['/S'], '/URI')
            self.assertEqual(actions[4]['/URI'], 'https://example.org/')


if __name__ == '__main__':
    unittest.main()
