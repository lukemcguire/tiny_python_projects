#!/usr/bin/env python3
"""
Author : Luke McGuire <luke.mcguire@gmail.com>
Date   : 2024-06-27
Purpose: Telephone
"""

import argparse
import os
import random
import string


# --------------------------------------------------
def float_percentage(s):
    """check for float between 0 and 1"""
    try:
        value = float(s)
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"invalid float value: '{s}'") from e
    if value < 0 or value >= 1:
        raise argparse.ArgumentTypeError(f'"{value}" must be between 0 and 1')
    return value


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Telephone", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("text", metavar="text", help="Input text or file")

    parser.add_argument("-s", "--seed", help="Random seed", metavar="int", type=int)

    parser.add_argument(
        "-m",
        "--mutations",
        help="Percent mutations",
        metavar="float",
        type=float_percentage,
        default=0.1,
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
    random.seed(args.seed)
    num_mutations = round(len(text) * args.mutations)
    alpha = "".join(sorted(string.ascii_letters + string.punctuation))
    scrambled = list(text)
    for i in random.sample(range(len(text)), k=num_mutations):
        scrambled[i] = random.choice(alpha.replace(text[i], ""))

    scrambled = "".join(scrambled)

    print(f'You said: "{text}"')
    print(f'I heard : "{scrambled}"')


# --------------------------------------------------
if __name__ == "__main__":
    main()
