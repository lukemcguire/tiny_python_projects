#!/usr/bin/env python3
"""
Author : Luke McGuire <luke.mcguire@gmail.com>
Date   : 2024-06-26
Purpose: A Shakesperean insult generator
"""

import argparse
import random


# --------------------------------------------------
def positive_int(string):
    """check for positive integer"""
    try:
        value = int(string)
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"invalid int value: '{string}'") from e
    if value < 1:
        raise argparse.ArgumentTypeError(f'"{value}" must be > 0')
    return value


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="A Shakesperean insult generator",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-a",
        "--adjectives",
        help="Number of adjectives",
        metavar="int",
        type=positive_int,
        default=2,
    )

    parser.add_argument(
        "-n",
        "--number",
        help="Number of insults",
        metavar="int",
        type=positive_int,
        default=3,
    )

    parser.add_argument("-s", "--seed", help="Random seed", metavar="int", type=int)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    adjectives = """
bankrupt base caterwauling corrupt cullionly detestable dishonest false
filthsome filthy foolish foul gross heedless indistinguishable infected
insatiate irksome lascivious lecherous loathsome lubbery old peevish
rascaly rotten ruinous scurilous scurvy slanderous sodden-witted
thin-faced toad-spotted unmannered vile wall-eyed""".split()

    nouns = """
Judas Satan ape ass barbermonger beggar block boy braggart butt
carbuncle coward coxcomb cur dandy degenerate fiend fishmonger fool
gull harpy jack jolthead knave liar lunatic maw milksop minion
ratcatcher recreant rogue scold slave swine traitor varlet villain worm""".split()

    args = get_args()
    random.seed(args.seed)

    for _ in range(args.number):
        descriptors = ", ".join(random.sample(adjectives, args.adjectives))
        print(f"You {descriptors} {random.choice(nouns)}!")


# --------------------------------------------------
if __name__ == "__main__":
    main()
