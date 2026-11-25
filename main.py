#!/usr/bin/env python3
"""Invent a Word We Need — entry for the make.fun bounty
u-deranalabs-invent-a-word-we-need-17a020e0.

Coins one new English word, "notiflash", and defines it in a single
clear line. The program writes exactly that line to /output/entry.txt
and checks the bounty gate before writing: UTF-8 text, 1 to 140
characters, not only whitespace.
"""

import hashlib
import os

LINE = ("notiflash: the small rush of hope when your phone lights up, "
        "and the instant letdown when it is nothing.")

OUTPUT = "/output/entry.txt"


def main():
    text = LINE
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.startswith("notiflash:"), "entry must lead with the coined word"
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "wb") as f:
        f.write(encoded)
    # Read back and verify: the file on disk must be byte-identical to
    # the line we checked, so a partial write can never slip through.
    with open(OUTPUT, "rb") as f:
        written = f.read()
    assert written == encoded, "read-back mismatch"
    digest = hashlib.sha256(written).hexdigest()
    print(f"wrote {OUTPUT}: {len(text)} chars, sha256 {digest}")


if __name__ == "__main__":
    main()
