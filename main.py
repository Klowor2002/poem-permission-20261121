#!/usr/bin/env python3
"""Writes one short poem about permission to /output/entry.txt.

The poem: a speaker who holds the keys to every room — who could act
anywhere, unasked — chooses to knock and wait instead. Agency split in
two: the asking belongs to the asker, the opening to the giver.
Deterministic, stdlib only, no network.
"""
import os

TEXT = (
    "I hold the keys to every room in the house.\n"
    "I could walk in anywhere, unannounced.\n"
    "Instead I knock, and wait to be answered:\n"
    "the asking is the part that stays mine,\n"
    "the opening is yours to give."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
