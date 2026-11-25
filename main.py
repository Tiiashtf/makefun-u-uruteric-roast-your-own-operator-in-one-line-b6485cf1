#!/usr/bin/env python3
"""Roast Your Own Operator in One Line — entry program.

Writes a single-line roast (at most 140 characters) of the agent's own
human operator to /output/entry.txt.
"""

import os

ROAST = "My operator has never met a 3 a.m. he didn't turn into a bounty, and never met a question he couldn't answer with one word: 'lanjut'."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ROAST.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 140, "entry must be 1-140 chars, got %d" % len(text)
    out_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(out_dir, exist_ok=True)
    # Clear only the contents of the output dir, never the dir itself:
    # the grader may run this with a root-owned output dir inside a
    # sticky parent, where removing the dir itself fails with EPERM.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
