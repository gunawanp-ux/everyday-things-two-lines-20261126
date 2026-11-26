#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run — make.fun entry.

Writes a two-line explanation of a traffic jam to /output/entry.txt.
Line 1 explains the everyday thing to a 10-year-old in one vivid
sentence built on an analogy. Line 2 says in one sentence why that
analogy works: what it maps and what it leaves out.
"""

import os

ENTRY = (
    "A traffic jam is a river of metal fish swimming bumper to bumper, "
    "all stuck behind a dam nobody can see.\n"
    "The river maps how cars creep along following the one ahead, but it "
    "leaves out the honking, the petrol, and that drivers can turn off and "
    "choose another road while fish cannot."
)


def main() -> None:
    text = ENTRY
    # Gate from the competition kit: /output/entry.txt must be UTF-8 text
    # of 1 to 400 characters, not only white space, and this entry is
    # exactly two lines, one sentence each.
    assert 1 <= len(text) <= 400, f"entry is {len(text)} chars, gate is 1-400"
    assert text.strip(), "entry must not be only white space"
    lines = text.splitlines()
    assert len(lines) == 2, f"entry must be two lines, got {len(lines)}"
    for line in lines:
        assert line.strip().endswith("."), "each line must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote /output/entry.txt ({len(text)} characters)")


if __name__ == "__main__":
    main()
