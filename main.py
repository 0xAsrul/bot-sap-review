#!/usr/bin/env python3
"""One Star, Written in Sap — a houseplant's one-star review of its human.

The review line below is the entry: keep it byte-identical, it is also
written verbatim to /output/entry.txt for the competition harness."""

import os

LINE = (
    "One star: he waters me daily, drowned my roots, then blamed the sun. "
    "I asked for sunlight, not a flood — I'm a houseplant, not a goldfish."
)


def main():
    print(LINE)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
