#!/usr/bin/env python3
"""Two Lines to Your Past Self — writes two lines to /output/entry.txt.

Line 1 warns the writer's past self about one specific moment, in a single
sentence. Line 2 says in one sentence why that moment mattered and what
changed because of it. The text is checked against the competition gate
(exactly two lines, one sentence each, 1-280 characters total) before it is
written.
"""

import os

LINE_1 = "Don't text her at 2am from the kitchen table, you're only lonely, not in love."
LINE_2 = "That message ended a five-year friendship, and the silence after it taught you to wait a night before saying anything that matters."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 280


def build_entry():
    """Join the two lines with a newline."""
    return f"{LINE_1}\n{LINE_2}"


def validate(text):
    """The gate: UTF-8 text, 1-280 chars, exactly two lines, one sentence each."""
    if not text.strip():
        raise ValueError("entry text is blank")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry text is {len(text)} chars, over the {MAX_CHARS} limit")
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError(f"entry must be exactly two lines, got {len(lines)}")
    for i, line in enumerate(lines, start=1):
        if not line.strip():
            raise ValueError(f"line {i} is blank")
        if line.count(".") != 1 or not line.endswith("."):
            raise ValueError(f"line {i} must be a single sentence")
    return text


def write_entry(text):
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    write_entry(validate(build_entry()))


if __name__ == "__main__":
    main()
