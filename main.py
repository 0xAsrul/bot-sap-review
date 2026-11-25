#!/usr/bin/env python3
"""One Star, Written in Sap — a houseplant's one-star review of its human."""

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
