#!/usr/bin/env python3
"""
Author : Luke McGuire <luke.mcguire@gmail.com>
Date   : 2024-06-28
Purpose: Ransom Note
"""

import argparse
import os
import random

# import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Ransom Note",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", help="Input text or file")
    parser.add_argument("-s", "--seed", help="Random seed", metavar="int", type=int)

    args = parser.parse_args()
    if os.path.isfile(args.text):
        with open(args.text, "rt", encoding="utf-8") as fh:
            args.text = fh.read().rstrip()

    return args


# --------------------------------------------------
def choose(char: str) -> str:
    """Choose a random case for a character"""

    return random.choice([char.lower(), char.upper()])


# --------------------------------------------------
def test_choose():
    """Test choose"""

    state = random.getstate()
    random.seed(1)
    assert choose("a") == "a"
    assert choose("b") == "b"
    assert choose("c") == "C"
    assert choose("d") == "d"
    random.setstate(state)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    print("".join(map(choose, args.text)))


# --------------------------------------------------
if __name__ == "__main__":
    main()
