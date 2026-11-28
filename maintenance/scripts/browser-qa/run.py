#!/usr/bin/env python3
"""Run browser checks against selected outputs and record their provenance."""
import hashlib
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
IMAGE = os.environ.get('BROWSER_QA_IMAGE', 'localhost/primers-browser-qa:1.61.1')
OCI = os.environ.get('OCI', 'podman')


def command(*args):
    return subprocess.check_output(args, cwd=ROOT, text=True).strip()


def describe_file(file):
    name = file.relative_to(ROOT).as_posix()
    digest = hashlib.sha256(file.read_bytes()).hexdigest()
    tracked = subprocess.run(['git', 'ls-files', '--error-unmatch', '--', name],
                             cwd=ROOT, capture_output=True).returncode == 0
    if tracked:
        current = command('git', 'hash-object', '--', name)
        baseline = subprocess.run(['git', 'rev-parse', f'HEAD:{name}'], cwd=ROOT,
                                  text=True, capture_output=True)
        binding = 'matches HEAD' if baseline.returncode == 0 and baseline.stdout.strip() == current else 'differs from HEAD'
    else:
        binding = 'untracked or ignored; not bound to HEAD'
    print('SHA256:', digest, name, f'({binding})', flush=True)


def main(paths):
    if not paths:
        raise ValueError('Select one or more repository-relative HTML output paths')
    selected = []
    for item in paths:
        file = (ROOT / item).resolve()
        if not file.is_relative_to(ROOT) or not file.is_file() or file.suffix != '.html':
            raise ValueError(f'Invalid repository HTML output: {item}')
        selected.append(file.relative_to(ROOT).as_posix())
    print('Revision:', command('git', 'rev-parse', 'HEAD'), flush=True)
    status = command('git', 'status', '--porcelain=v1', '--untracked-files=normal')
    print('Working tree:', 'clean' if not status else 'dirty\n' + status, flush=True)
    print('Image:', IMAGE, command(OCI, 'image', 'inspect', IMAGE, '--format', '{{.Id}}'), flush=True)
    for name in selected:
        describe_file(ROOT / name)
        sibling = (ROOT / name).with_name((ROOT / name).name.removesuffix('.html').removesuffix('.mathjax') + '.mathml.html')
        if sibling.is_file() and sibling != ROOT / name:
            describe_file(sibling)
    mount = f'{ROOT}:/repo:ro' + (',z' if OCI == 'podman' else '')
    args = [OCI, 'run', '--rm', '--network', 'none', '-v', mount, IMAGE, *selected]
    print('Command:', subprocess.list2cmdline(args), flush=True)
    return subprocess.run(args, cwd=ROOT, check=False).returncode


if __name__ == '__main__':
    try:
        sys.exit(main(sys.argv[1:]))
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(f'ERROR: {error}', file=sys.stderr)
        sys.exit(2)
