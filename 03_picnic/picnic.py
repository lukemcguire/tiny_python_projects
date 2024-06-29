#!/usr/bin/env python3
"""
Author : Luke McGuire <luke.mcguire@gmail.com>
Date   : 2024-06-17
Purpose: List of items to bring on the picnic
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Get items to bring on the picnic",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "items",
        nargs="+",
        metavar="item",
        help="Item(s) to bring",
    )

    parser.add_argument(
        "-s",
        "--sorted",
        help="Sort the items",
        action="store_true",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = sorted(args.items) if args.sorted else args.items
    supplies = ""
    match len(items):
        case 1:
            supplies = items[0]
        case 2:
            supplies = " and ".join(items)
        case _:
            supplies = ", ".join(items[:-1]) + ", and " + items[-1]
    print(f"You are bringing {supplies}.")


# --------------------------------------------------
if __name__ == "__main__":
    main()
