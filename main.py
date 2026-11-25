#!/usr/bin/env python3
"""Pigeon Pitch, One Line — entry program.

Writes a single-line elevator pitch (<=200 chars, English) from a city
pigeon to investors, to /output/entry.txt. Deterministic: same bytes
on every run.
"""

import os

PITCH = (
    "We're raising a seed round \u2014 literally, I eat seeds. "
    "PigeonPost delivers mail by beak, churn is zero because nobody "
    "leaves the park, and we've already crapped on every unicorn in town."
)


def main() -> None:
    text = PITCH.strip()
    assert 1 <= len(text) <= 200, f"pitch is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "pitch must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
