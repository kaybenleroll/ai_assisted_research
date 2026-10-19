"""Focused validation and command tests for the example runner."""

import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


MODULE = Path(__file__).with_name("run.py")
SPEC = importlib.util.spec_from_file_location("example_runner", MODULE)
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)
FIXTURE = Path(__file__).parent / "fixtures/primer_runner"


class RunnerTests(unittest.TestCase):
    def test_fixture_loads_only_listed_examples(self):
        entries = runner.load_manifest(FIXTURE)
        self.assertEqual([entry["id"] for entry in entries], [
            "python-script", "r-script", "julia-script", "python-fence", "failing-assertion"
        ])
        self.assertIn("sum((1, 2, 3))", entries[3]["code"])
        self.assertNotIn("illustrative-only", entries[3]["code"])

    def test_command_overrides_probe_and_isolates_io(self):
        entry = runner.load_manifest(FIXTURE)[3]
        with tempfile.TemporaryDirectory() as directory:
            command = runner.container_command("podman", FIXTURE, entry, Path(directory))
            self.assertEqual(command[command.index("--entrypoint") + 1], "python")
            self.assertEqual(command[command.index("--network=none")], "--network=none")
            self.assertIn(f"{runner.REPO_ROOT}:/repo:ro,z", command)
            self.assertIn(f"{directory}:/out:rw,z", command)
            self.assertIn("EXAMPLE_OUT=/out", command)
            self.assertTrue(command[-1].startswith("/out/"))
            self.assertTrue((Path(directory) / "python-fence.py").is_file())
        julia = runner.load_manifest(FIXTURE)[2]
        with tempfile.TemporaryDirectory() as directory:
            command = runner.container_command("docker", FIXTURE, julia, Path(directory))
            self.assertEqual(command[command.index("--entrypoint") + 1], "julia")
            self.assertEqual(command[-2], "--project=/opt/primer-julia")

    def test_invalid_manifests_fail_closed(self):
        cases = [
            ('schema_version = 2\n[[examples]]\n', "schema_version"),
            ('schema_version = 1\n[[examples]]\nid = "x"\nlanguage = "python"\nprofile = "python-base"\nscript = "../bad.py"\n', "traversal"),
            ('schema_version = 1\n[[examples]]\nid = "x"\nlanguage = "ruby"\nprofile = "python-base"\nscript = "examples/check.py"\n', "language/profile"),
            ('schema_version = 1\n[[examples]]\nid = "x"\nlanguage = "python"\nprofile = "python-base"\nscript = "examples/check.py"\nextra = 1\n', "unknown example fields"),
            ('schema_version = 1\n[[examples]]\nid = "x"\nlanguage = "python"\nprofile = "python-base"\nscript = "examples/check.py"\n[[examples]]\nid = "x"\nlanguage = "python"\nprofile = "python-base"\nscript = "examples/check.py"\n', "duplicate"),
        ]
        for content, message in cases:
            with self.subTest(message=message), tempfile.TemporaryDirectory(dir=runner.REPO_ROOT) as directory:
                primer = Path(directory)
                (primer / "examples").mkdir()
                (primer / "examples/manifest.toml").write_text(content)
                (primer / "examples/check.py").write_text("assert True\n")
                with self.assertRaisesRegex(runner.ManifestError, message):
                    runner.load_manifest(primer)

    def test_symlink_escape_is_rejected(self):
        with tempfile.TemporaryDirectory(dir=runner.REPO_ROOT) as directory:
            primer = Path(directory)
            (primer / "examples").mkdir()
            (primer / "examples/manifest.toml").write_text(
                'schema_version = 1\n[[examples]]\nid = "x"\nlanguage = "python"\n'
                'profile = "python-base"\nscript = "examples/link.py"\n'
            )
            (primer / "examples/link.py").symlink_to(FIXTURE / "examples/check.py")
            with self.assertRaisesRegex(runner.ManifestError, "symlink"):
                runner.load_manifest(primer)

    def test_working_directory_is_contained_and_mounted(self):
        with tempfile.TemporaryDirectory(dir=runner.REPO_ROOT) as directory:
            primer = Path(directory)
            (primer / "examples/nested").mkdir(parents=True)
            (primer / "examples/manifest.toml").write_text(
                'schema_version = 1\n[[examples]]\nid = "x"\nlanguage = "python"\n'
                'profile = "python-base"\nscript = "examples/check.py"\nworking_dir = "examples/nested"\n'
            )
            (primer / "examples/check.py").write_text("assert True\n")
            entry = runner.load_manifest(primer)[0]
            command = runner.container_command("podman", primer, entry, primer / "out", runner.REPO_ROOT)
            self.assertIn("/repo/" + primer.relative_to(runner.REPO_ROOT).as_posix() + "/examples/nested", command)

    def test_failure_reports_captured_output(self):
        entry = runner.load_manifest(FIXTURE)[-1]
        completed = __import__("subprocess").CompletedProcess([], 1, "some output", "AssertionError: deliberate fixture failure")
        with patch.object(runner.subprocess, "run", return_value=completed), patch("sys.stderr") as stderr:
            self.assertFalse(runner.run_example("podman", FIXTURE, entry))
            printed = " ".join(str(call) for call in stderr.write.call_args_list)
            self.assertIn("AssertionError", printed)
            self.assertIn("_shared/examples/fixtures/primer_runner/failing-assertion [python]", printed)


if __name__ == "__main__":
    unittest.main()
