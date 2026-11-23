#!/usr/bin/env python3
"""One Line, Best Line — write the entry line to the output directory.

The program writes a single line of text to entry.txt in the output
directory: the MAKEFUN_OUTPUT_DIR environment variable when set,
otherwise /output. The line is a fixed constant, so every run produces
byte-identical output.
"""

import os
import sys

LINE = (
    "The cat pays no rent, fears no god, and sleeps sixteen hours a day: "
    "evolution peaked, and it's asleep on my laundry."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
