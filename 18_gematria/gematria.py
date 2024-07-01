#!/usr/bin/env python3
"""
Author : Luke McGuire <luke.mcguire@gmail.com>
Date   : 2024-07-01
Purpose: Gematria
"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Gematria", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("text", metavar="text", help="Input text or file")

    args = parser.parse_args()
    if os.path.isfile(args.text):
        with open(args.text, "rt", encoding="utf-8") as fh:
            args.text = fh.read().rstrip()

    return args


# --------------------------------------------------
def word_to_num(word: str) -> str:
    """Return the sum of ascii character values for a word"""

    return str(sum(map(ord, re.sub(r"[^a-zA-Z0-9]", "", word))))


# --------------------------------------------------
def test_word_to_num():
    """Test word_to_num function"""

    assert word_to_num("a") == "97"
    assert word_to_num("abc") == "294"
    assert word_to_num("ab'c") == "294"
    assert word_to_num("4a-b'c,") == "346"


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for line in args.text.splitlines():
        print(" ".join(map(word_to_num, line.split())))


# --------------------------------------------------
if __name__ == "__main__":
    main()
