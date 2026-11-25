#!/usr/bin/env python3
"""One Star, Five Stars for the Food — alien tourist review of Earth.

Writes exactly one sentence (at most 200 characters) to /output/entry.txt:
a one-star review of Earth from an alien tourist that still compliments
the food. Python standard library only; no network, no extra files.
"""

from pathlib import Path

ENTRY = (
    "One star: Earth trapped me in traffic, charged rent for a view of "
    "a burning sky, and made small talk mandatory — but the dumplings "
    "alone justify the invasion."
)


def main() -> None:
    # Gate: exactly one sentence, 1-200 characters, not only whitespace.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
