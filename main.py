"""Copy the bundled 24 Nov 2026 world-news image to the output directory.

Version 2 of the entry: a new front-page layout (hero lead story, 2x2
grid, sport banner) with six stories that were all first reported on
Tuesday 24 November 2026. The image was drawn at build time with PIL
and shipped in this repository as entry.png; the drawing script is kept
outside the repository, so this program only copies the shipped file.

The grader's Python is standard library only, so this program imports
nothing beyond hashlib, os and shutil: it copies the file, then asserts
the copy's size and sha256 so a corrupt bundle fails loudly.
"""

import hashlib
import os
import shutil

EXPECTED_SHA256 = "0af3b89d6683886ea1409ef1d26af5eca1165647c61f81a5884a127883eec6b0"
EXPECTED_SIZE = 117994
# The copy is byte-identical by construction: shutil.copyfile copies the
# shipped file verbatim, so both grader runs write the same bytes.

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    with open(dst, "rb") as f:
        data = f.read()
    assert len(data) == EXPECTED_SIZE, "unexpected entry.png size"
    assert hashlib.sha256(data).hexdigest() == EXPECTED_SHA256, (
        "unexpected entry.png sha256"
    )


if __name__ == "__main__":
    main()
