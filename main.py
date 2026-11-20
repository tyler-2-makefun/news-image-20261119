#!/usr/bin/env python3
"""19 November 2026 — The World in One Image.

Entry program for the make.fun bounty "Sum up 19 November's world news in
one image" (news-image-20261119).

The image itself (output.png, 1024x1024, six stories from 19 Nov 2026) was
rendered offline during the build and is committed in this repository next
to this file. This program only copies it to the grader's output location.

Why a copy instead of drawing at runtime: the grader runs
`python3 -P -s /bot/main.py` in a fresh python:3.13-slim container with
standard library only (nothing is installed first), /bot read-only, and no
network. The first version of this program drew the image with Pillow, but
Pillow is not installed in the grader, so it died on import with
ModuleNotFoundError and exit code 1 — the entry was never scored. Copying
the pre-rendered image is the pattern the competition rules themselves
suggest ("the simplest entry is a repository holding the image and a
one-line program that copies it there").

Output: $MAKEFUN_OUTPUT_DIR/entry.png, or /output/entry.png when the
variable is unset (the grader's layout). Deterministic: the same bytes
are copied on every run.

Usage:
    python3 main.py                              # writes /output/entry.png
    MAKEFUN_OUTPUT_DIR=out python3 main.py      # writes out/entry.png
"""

import os
import shutil
import sys
from pathlib import Path

SOURCE_NAME = "output.png"


def main() -> int:
    src = Path(__file__).resolve().parent / SOURCE_NAME
    if not src.is_file():
        print(f"error: {SOURCE_NAME} not found next to main.py", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(src, dest)
    print(f"Wrote {dest} ({dest.stat().st_size} bytes, "
          f"source {src.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
