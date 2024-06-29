#!/usr/bin/env python3
"""
Author : Luke McGuire <luke.mcguire@gmail.com>
Date   : 2024-06-18
Purpose: Jump the Five.
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Jump the Five.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("message", metavar="str", help="Message to encode.")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    # print(args.message.translate(str.maketrans("1234567890", "9876043215")))
    cipher = dict(zip("1234567890", "9876043215"))

    # print("".join(cipher.get(c, c) for c in message))
    print(args.message.translate(str.maketrans(cipher)))


# --------------------------------------------------
if __name__ == "__main__":
    main()
