#!/usr/bin/env python3
"""
Author : Luke McGuire <luke.mcguire@gmail.com>
Date   : 2024-07-01
Purpose: Scramble the letters of words
"""

import argparse
import os
import random
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Scramble the letters of words",
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
def shuffle(word):
    """Scramble the inside letters of a word"""
    if len(word) > 3 and re.match(r"\w+", word):
        first, middle, last = word[0], list(word[1:-1]), word[-1]
        random.shuffle(middle)
        word = first + "".join(middle) + last
    return word


# --------------------------------------------------
def test_shuffle():
    """Test the shuffle function"""
    state = random.getstate()
    random.seed(1)

    assert shuffle("") == ""
    assert shuffle("a") == "a"
    assert shuffle("at") == "at"
    assert shuffle("hat") == "hat"
    assert shuffle("potato") == "ptoato"
    assert shuffle("scrambled") == "slerbmcad"

    random.setstate(state)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    splitter = re.compile(r"([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")

    for line in args.text.splitlines():
        print("".join(map(shuffle, splitter.split(line))))


# --------------------------------------------------
if __name__ == "__main__":
    main()
