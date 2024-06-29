#!/usr/bin/env python3
"""
Author : Luke McGuire <luke.mcguire@gmail.com>
Date   : 2024-06-28
Purpose: Twelve Days of Christmas
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Twelve Days of Christmas",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-n",
        "--num",
        help="Nmber of days to sing",
        metavar="days",
        type=int,
        default=12,
    )

    parser.add_argument(
        "-o",
        "--outfile",
        help="Output filename",
        metavar="FILE",
        type=argparse.FileType("wt"),
        default=sys.stdout,
    )

    args = parser.parse_args()

    if args.num < 1 or args.num > 12:
        parser.error(f'--num "{args.num}" must be between 1 and 12')

    return args


# --------------------------------------------------
def verse(day: int) -> str:
    """Return the verse of the Twelve Days of Christmas for a given day"""
    ordinal = {
        1: "first",
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth",
        9: "ninth",
        10: "tenth",
        11: "eleventh",
        12: "twelfth",
    }

    gifts = {
        1: "And a partridge in a pear tree.",
        2: "Two turtle doves,",
        3: "Three French hens,",
        4: "Four calling birds,",
        5: "Five gold rings,",
        6: "Six geese a laying,",
        7: "Seven swans a swimming,",
        8: "Eight maids a milking,",
        9: "Nine ladies dancing,",
        10: "Ten lords a leaping,",
        11: "Eleven pipers piping,",
        12: "Twelve drummers drumming,",
    }

    lyrics = [f"On the {ordinal[day]} day of Christmas,", "My true love gave to me,"]

    if day == 1:
        lyrics.append("A partridge in a pear tree.")
    else:
        for d in range(day, 0, -1):
            lyrics.append(gifts[d])

    return "\n".join(lyrics)


# --------------------------------------------------
def test_verse_1():
    """Test the verse function for day 1"""
    one = "\n".join(
        [
            "On the first day of Christmas,",
            "My true love gave to me,",
            "A partridge in a pear tree.",
        ]
    )
    assert verse(1) == one


def test_verse_2():
    """Test the verse function for day 2"""
    two = "\n".join(
        [
            "On the second day of Christmas,",
            "My true love gave to me,",
            "Two turtle doves,",
            "And a partridge in a pear tree.",
        ]
    )
    assert verse(2) == two


def test_verse_12():
    """Test the verse function for day 12"""
    twelve = "\n".join(
        [
            "On the twelfth day of Christmas,",
            "My true love gave to me,",
            "Twelve drummers drumming,",
            "Eleven pipers piping,",
            "Ten lords a leaping,",
            "Nine ladies dancing,",
            "Eight maids a milking,",
            "Seven swans a swimming,",
            "Six geese a laying,",
            "Five gold rings,",
            "Four calling birds,",
            "Three French hens,",
            "Two turtle doves,",
            "And a partridge in a pear tree.",
        ]
    )
    assert verse(12) == twelve


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    song = "\n\n".join(map(verse, range(1, args.num + 1)))
    print(song, file=args.outfile)


# --------------------------------------------------
if __name__ == "__main__":
    main()
