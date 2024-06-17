#!/usr/bin/env python3
"""
Author : Oak Hopper
Date   : 2024-06-17
Purpose: Say Hello
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Say hello",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-n", "--name", help="Name to greet", metavar="name", type=str, default="World"
    )
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(f"Hello, {args.name}!")


# --------------------------------------------------
if __name__ == "__main__":
    main()
