#!/usr/bin/env python3
"""
Author : Luke McGuire <luke.mcguire@gmail.com>
Date   : 2024-06-28
Purpose: Bottles of beer song
"""

import argparse


# --------------------------------------------------
def positive_int(string):
    """check for positive integer"""
    try:
        value = int(string)
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"invalid int value: '{string}'") from e
    if value < 1:
        raise argparse.ArgumentTypeError(f'"{value}" must be greater than 0')
    return value


# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Bottles of beer song",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-n",
        "--num",
        help="How many bottles",
        metavar="int",
        type=positive_int,
        default=10,
    )

    return parser.parse_args()


# --------------------------------------------------
def verse(bottle: int) -> str:
    """Sing a verse"""

    next_bottle = bottle - 1
    s1 = "" if bottle == 1 else "s"
    s2 = "" if next_bottle == 1 else "s"

    lyrics = [
        f"{bottle} bottle{s1} of beer on the wall,",
        f"{bottle} bottle{s1} of beer,",
        "Take one down, pass it around,",
        f"{next_bottle if next_bottle else 'No more'} bottle{s2} of beer on the wall!",
    ]
    return "\n".join(lyrics)


# --------------------------------------------------
def test_verse_1():
    """Test verse for 1 bottle"""

    one = verse(1)
    assert one == "\n".join(
        [
            "1 bottle of beer on the wall,",
            "1 bottle of beer,",
            "Take one down, pass it around,",
            "No more bottles of beer on the wall!",
        ]
    )


def test_verse_2():
    """Test verse for 2 bottles"""

    two = verse(2)
    assert two == "\n".join(
        [
            "2 bottles of beer on the wall,",
            "2 bottles of beer,",
            "Take one down, pass it around,",
            "1 bottle of beer on the wall!",
        ]
    )


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    # song = map(verse, range(args.num, 0, -1))
    print("\n\n".join(song))


# --------------------------------------------------
if __name__ == "__main__":
    main()
