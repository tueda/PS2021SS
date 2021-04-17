"""Convert notebooks into different formats."""

import logging
import subprocess
import time
from pathlib import Path

import joblib

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


def convert(notebook_dir: Path, dest_dir: Path, fmt: str, clear: bool = True):
    """Convert notebooks into another format."""
    if fmt == "html":
        fmt_name = "HTML"
        fmt_opts = ["--to", "html", "--template", "lab"]
    elif fmt == "md":
        fmt_name = "Markdown"
        fmt_opts = ["--to", "markdown"]
    else:
        raise ValueError(f"format {fmt} unsupported")

    t1 = time.time()

    if clear:
        # Clear the destination directory.
        dest_dir.mkdir(exist_ok=True)
        for child in dest_dir.glob("*"):
            if child.is_file():
                child.unlink()

    # Collect .ipynb files to be converted.

    target_files = []

    for child in notebook_dir.glob("*"):
        if child.is_file() and child.suffix == ".ipynb":
            target_files.append(child)

    # Convert the .ipynb files.

    def run(target: Path):
        subprocess.run(  # noqa: S603, S607
            [
                "jupyter",
                "nbconvert",
                *fmt_opts,
                "--output-dir",
                str(dest_dir),
                str(target),
            ]
        )

    joblib.Parallel(n_jobs=-1)(joblib.delayed(run)(f) for f in target_files)

    t2 = time.time()

    logger.info(f"Notebooks converted to {fmt_name} in {t2 - t1:.3f} seconds")


def nb2html(*args, **kwargs) -> None:
    """Generate HTML files from notebooks for previews."""
    docs_dir = Path(kwargs["config"]["docs_dir"])

    notebook_dir = docs_dir / "notebooks"
    preview_dir = docs_dir / "previews"

    convert(notebook_dir, preview_dir, "html", clear=True)


def nb2md() -> None:
    """Generate Markdown files from notebooks for textlint."""
    root_dir = Path(".")

    notebook_dir = root_dir / "notebooks"
    dest_dir = root_dir / ".converted"

    convert(notebook_dir, dest_dir, "md", clear=False)
