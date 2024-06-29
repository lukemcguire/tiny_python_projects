#!/usr/bin/env python3
"""
Author : Luke McGuire <luke.mcguire@gmail.com>
Date   : 2024-06-21
Purpose: Prints the line from a file starting with a given letter.
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Gashlycrumb",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("letter", metavar="letter", nargs="+", help="Letter(s)")

    parser.add_argument(
        "-f",
        "--file",
        help="Input file",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default="gashlycrumb.txt",
    )
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    my_dict = {}
    for i, line in enumerate(args.file):
        my_dict[line[0].lower()] = line.strip()

    for l in args.letter:
        text = my_dict.get(l.lower())
        if text:
            print(my_dict[l.lower()])
        else:
            print(f'I do not know "{l}".')


# --------------------------------------------------
if __name__ == "__main__":
    main()
