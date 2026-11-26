#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes a single roast line (1-160 characters) to /output/entry.txt.
Python 3.13 standard library only, no network at run time.

The line: a smart fridge whose touchscreen froze. One concrete
behaviour, one sting at the end, nothing explained.
"""

import os
from pathlib import Path

ENTRY = "My smart fridge's touchscreen froze \u2014 the irony is the only thing still running."

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    # Gate assertions: exactly one line, 1-160 characters, non-empty.
    assert ENTRY, "entry must not be empty"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 160, f"entry must be 1-160 chars, got {len(ENTRY)}"
    assert ENTRY.strip() == ENTRY, "entry must not be only whitespace"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUTPUT_DIR / "entry.txt"
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
