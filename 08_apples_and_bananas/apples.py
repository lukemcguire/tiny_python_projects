#!/usr/bin/env python3
"""
Author : Luke McGuire <luke.mcguire@gmail.com>
Date   : 2024-06-26
Purpose: Apples and Bananas
"""

import argparse
import os
import re

# import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Apples and Bananas",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "text",
        help="Input text or file",
        metavar="text",
    )

    parser.add_argument(
        "-v",
        "--vowel",
        help="A named string argument",
        metavar="str",
        type=str,
        default="a",
        choices=list("aeiou"),
    )

    args = parser.parse_args()
    if os.path.isfile(args.text):
        with open(args.text, "rt", encoding="utf-8") as fh:
            args.text = fh.read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text

    text = re.sub("[aeiou]", args.vowel, text)
    text = re.sub("[AEIOU]", args.vowel.upper(), text)

    print(text)


# --------------------------------------------------
if __name__ == "__main__":
    main()
