#!/usr/bin/env python3
"""
Author : Luke McGuire <luke.mcguire@gmail.com>
Date   : 2024-06-29
Purpose: Southern fry text
"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Southern fry text",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", help="Input text or file")

    args = parser.parse_args()
    if os.path.isfile(args.text):
        with open(args.text, "rt", encoding="utf-8") as fh:
            args.text = fh.read().rstrip()

    return args


# --------------------------------------------------
def fry(word):
    """Drog the g from -ing word, you to y'all"""
    you_match = re.match(r"([Yy])ou", word)
    ing_match = re.match(r"(^\w*[aeiou]+\w*in)g$", word, flags=re.I)
    if you_match:
        word = you_match.group(1) + "'all"
    elif ing_match:
        word = ing_match.group(1) + "'"

    return word


# --------------------------------------------------
def test_fry():
    """Test fry"""

    assert fry("") == ""
    assert fry("you") == "y'all"
    assert fry("You") == "Y'all"
    assert fry("fishing") == "fishin'"
    assert fry("Aching") == "Achin'"
    assert fry("swing") == "swing"


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for line in args.text.splitlines():
        print("".join(map(fry, re.split(r"(\W+)", line.rstrip()))))


# --------------------------------------------------
if __name__ == "__main__":
    main()
