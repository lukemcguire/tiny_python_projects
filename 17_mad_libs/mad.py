#!/usr/bin/env python3
"""
Author : Luke McGuire <luke.mcguire@gmail.com>
Date   : 2024-07-01
Purpose: Mad Libs
"""

import argparse
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Mad Libs", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "-i",
        "--inputs",
        help="A named string argument",
        metavar="str",
        type=str,
        nargs="*",
    )

    parser.add_argument(
        "file", metavar="FILE", help="Input file", type=argparse.FileType("rt")
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    text = args.file.read().rstrip()

    placeholders = re.findall("(<([^<>]+?)>)", text)
    if not placeholders:
        print(f'"{args.file.name}" has no placeholders.', file=sys.stderr)
        sys.exit(1)

    inputs = iter(args.inputs)

    template = "Give me {} {}: "
    for placeholder, word in placeholders:
        article: str = "an" if word[0].lower() in "aeiou" else "a"
        answer = next(inputs) if inputs else input(template.format(article, word))
        text = re.sub(placeholder, answer, text, count=1)

    print(text)


# --------------------------------------------------
if __name__ == "__main__":
    main()
