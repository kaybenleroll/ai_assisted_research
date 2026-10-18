#!/usr/local/bin/python
"""Fail-closed probe for the shared executable-example Python images."""

from __future__ import annotations

import argparse
import importlib.metadata
import platform
import sys


def version(distribution: str) -> str:
    return importlib.metadata.version(distribution)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", choices=("base", "torch"), default="base")
    args = parser.parse_args()

    assert sys.version_info[:2] == (3, 12), sys.version
    import numpy as np
    import scipy

    assert np.allclose(np.array([1.0, 2.0]) @ np.array([[1.0], [2.0]]), [5.0])
    assert scipy.__version__ == version("scipy")
    packages = {
        "numpy": version("numpy"),
        "scipy": version("scipy"),
        "matplotlib": version("matplotlib"),
    }

    if args.profile == "torch":
        import torch

        assert torch.__version__.split("+")[0] == version("torch").split("+")[0]
        x = torch.tensor(3.0, requires_grad=True)
        value = x**2
        value.backward()
        assert torch.equal(x.grad, torch.tensor(6.0))
        packages["torch"] = version("torch")

    print(
        "primer-python-probe: "
        f"profile={args.profile} python={platform.python_version()} packages={packages}"
    )


if __name__ == "__main__":
    main()
