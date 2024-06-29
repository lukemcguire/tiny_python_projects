#!/usr/bin/env python3
"""
Author : Luke McGuire <luke.mcguire@gmail.com>
Date   : 2024-06-21
Purpose: Emulate wc (word count)
"""

import argparse
import sys
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Emulate wc (word count)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file",
        help="Input file(s)",
        nargs="*",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default=[sys.stdin],
    )

    args = parser.parse_args()

    # if args.file != [sys.stdin]:
    #     for path in args.file:
    #         if not os.path.isfile(path.name):
    #             print(f"No such file or directory: '{path.name}'")
    #             sys.exit()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    total_lines = 0
    total_words = 0
    total_bytes = 0

    for fh in args.file:
        num_lines = 0
        num_words = 0
        num_bytes = 0
        for line in fh:
            num_lines += 1
            num_words += len(line.split())
            num_bytes += len(line)

        print(f"{num_lines:>8}{num_words:>8}{num_bytes:>8} {fh.name}")
        total_lines += num_lines
        total_words += num_words
        total_bytes += num_bytes

    if len(args.file) > 1:
        print(f"{total_lines:>8}{total_words:>8}{total_bytes:>8} total")


# --------------------------------------------------
if __name__ == "__main__":
    main()
