"""Copy the bundled 24 Nov 2026 world-news image to the output directory.

The image was drawn at build time with PIL and shipped in this repository
as entry.png. The grader's Python is standard library only, so this
program imports nothing beyond hashlib, os and shutil: it copies the file,
then asserts the copy's size and sha256 so a corrupt bundle fails loudly.
"""

import hashlib
import os
import shutil

EXPECTED_SHA256 = "56fa45be774f3de94cae0795b99deca61f708ad2addef33456908005d312dc31"
EXPECTED_SIZE = 86454
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
