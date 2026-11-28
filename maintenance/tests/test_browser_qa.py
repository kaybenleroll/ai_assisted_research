"""Container integration tests for the browser QA recipe (run explicitly)."""
import hashlib
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
RUNNER = ROOT / 'maintenance/scripts/browser-qa/run.py'
PAGE = '''<!doctype html><html><body>
<a href="#main-content">Skip to main content</a>
<button id="math-mode-toggle" {renderer_attr}>Switch math renderer</button>
<noscript><a href="sample.mathml.html" {fallback_attr}>Read the MathML version</a></noscript>
<nav id="TOC" class="collapsible-ready" aria-label="Table of contents">
<button aria-expanded="false" aria-controls="sub" {toggle_attr}>Toggle subsections</button>
<a href="#intro" {link_attr}>Introduction</a><ul id="sub" hidden><li>Child</li></ul></nav>
<main id="main-content" tabindex="-1" aria-label="Document"><h1 id="intro">Introduction</h1><math><mi>x</mi></math></main>
<script>
const button = document.querySelector('#TOC button');
button.addEventListener('click', () => {{ const list = document.querySelector('#sub');
list.hidden = !list.hidden; button.setAttribute('aria-expanded', {expanded}); }});
document.querySelector('#math-mode-toggle').addEventListener('click', () => {{
  location.href = location.pathname.endsWith('.mathml.html') ? {reverse} : 'sample.mathml.html';
}});
</script></body></html>'''


class BrowserIntegration(unittest.TestCase):
    def setUp(self):
        (ROOT / '.scratch').mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=ROOT / '.scratch')
        self.folder = Path(self.temp.name)
        self.addCleanup(self.temp.cleanup)

    def make_pages(self, **changes):
        values = dict(renderer_attr='', fallback_attr='', toggle_attr='', link_attr='',
                      expanded="String(!list.hidden)", reverse="'sample.mathjax.html'")
        values.update(changes)
        html = PAGE.format(**values)
        for name in ('sample.html', 'sample.mathjax.html', 'sample.mathml.html'):
            (self.folder / name).write_text(html)

    def run_check(self, name):
        path = (self.folder / name).relative_to(ROOT).as_posix()
        return subprocess.run(['python3', '-I', str(RUNNER), path], cwd=ROOT,
                              capture_output=True, text=True, env=os.environ.copy(), timeout=60)

    def test_both_renderer_directions_and_provenance(self):
        self.make_pages()
        for page, destination in [('sample.html', 'MathML'), ('sample.mathml.html', 'MathJax')]:
            result = self.run_check(page)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn(f'PASS renderer control: Tab and Enter to {destination}', result.stdout)
            for file in (RUNNER, ROOT / 'maintenance/scripts/browser-qa/check.cjs'):
                self.assertIn(hashlib.sha256(file.read_bytes()).hexdigest(), result.stdout)
            self.assertIn('not bound to HEAD', result.stdout)

    def test_keyboard_controls_must_be_reachable(self):
        for attr, message in [('renderer_attr', 'renderer control'), ('toggle_attr', 'contents toggle'),
                              ('link_attr', 'contents link'), ('fallback_attr', 'MathML fallback')]:
            with self.subTest(control=attr):
                self.make_pages(**{attr: 'tabindex="-1"'})
                result = self.run_check('sample.html')
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertIn(message, result.stdout)

    def test_wrong_reverse_renderer_destination_fails(self):
        self.make_pages(reverse="'sample.html'")
        result = self.run_check('sample.mathml.html')
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn('FAIL', result.stdout)

    def test_wrong_forward_renderer_destination_fails(self):
        self.make_pages()
        page = self.folder / 'sample.html'
        page.write_text(page.read_text().replace(": 'sample.mathml.html'", ": 'sample.mathjax.html'"))
        result = self.run_check('sample.html')
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn('FAIL', result.stdout)

    def test_expanded_state_must_match_visibility(self):
        self.make_pages(expanded='String(list.hidden)')
        result = self.run_check('sample.html')
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn('aria-expanded disagrees with visibility', result.stdout)


if __name__ == '__main__':
    unittest.main()
