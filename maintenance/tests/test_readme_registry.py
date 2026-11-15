"""Focused checks for the generated README catalogue contract."""

import importlib.util
from pathlib import Path
import sys
import unittest


MODULE = Path(__file__).parents[1] / "scripts/update_readme_recent.py"
SPEC = importlib.util.spec_from_file_location("readme_registry", MODULE)
registry = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = registry
SPEC.loader.exec_module(registry)


class ReadmeRegistryTests(unittest.TestCase):
    def test_current_registry_is_unambiguous_and_safe(self):
        registry.validate_document_registry()
        registry.validate_primer_registry()

    def test_current_readme_is_generated_from_registry(self):
        current = registry.README.read_text(encoding="utf-8")
        self.assertEqual(registry.generate(current), current)

    def test_registry_rejects_duplicate_output_identity(self):
        original = registry.DOCUMENTS
        try:
            registry.DOCUMENTS = original + (original[0],)
            with self.assertRaisesRegex(ValueError, "Duplicate registry title"):
                registry.validate_document_registry()
        finally:
            registry.DOCUMENTS = original

    def test_registry_rejects_unsafe_paths(self):
        with self.assertRaisesRegex(ValueError, "repository-relative"):
            registry.checked_path("/tmp/out.html")
        with self.assertRaisesRegex(ValueError, "escapes repository"):
            registry.checked_path("../outside.html")

    def test_registry_rejects_table_breaking_text(self):
        original = registry.DOCUMENTS
        try:
            document = original[0]
            registry.DOCUMENTS = (registry.Document(
                document.title,
                document.category,
                "bad | cell",
                document.html,
                document.pdf,
                document.justfile,
                document.date_variable,
                document.catalogue_title,
                document.recent_priority,
            ), *original[1:])
            with self.assertRaisesRegex(ValueError, "unescaped pipe"):
                registry.validate_document_registry()
        finally:
            registry.DOCUMENTS = original


if __name__ == "__main__":
    unittest.main()
