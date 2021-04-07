"""MkDocs plugin hooks."""

import subprocess
from pathlib import Path


def nb2html(*args, **kwargs) -> None:
    """Generate HTML files from notebooks for previews."""
    docs_dir = Path(kwargs["config"]["docs_dir"])

    notebook_dir = docs_dir / "notebooks"
    preview_dir = docs_dir / "previews"

    preview_dir.mkdir(exist_ok=True)
    for child in preview_dir.glob("*"):
        if child.is_file():
            child.unlink()

    for child in notebook_dir.glob("*"):
        if child.is_file() and child.suffix == ".ipynb":
            subprocess.run(  # noqa: S603, S607
                [
                    "jupyter",
                    "nbconvert",
                    "--to",
                    "html",
                    "--template",
                    "lab",
                    "--output-dir",
                    str(preview_dir),
                    str(child),
                ]
            )
