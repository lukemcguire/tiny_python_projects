#!/usr/bin/env python3
"""
Author : Luke McGuire <luke.mcguire@gmail.com>
Date   : 2024-06-29
Purpose: Make rhyming "words"
"""

import argparse
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("str", metavar="str", help="A word to rhyme")

    return parser.parse_args()


# --------------------------------------------------
def stemmer(word: str):
    """Break a word into its leading consonants and the remainder"""
    pattern = re.compile(r"^([^aeiou]*)(.*)$")
    return pattern.search(word.lower()).groups()


# --------------------------------------------------
def test_stemmer():
    """Test stemmer"""
    assert stemmer("") == ("", "")
    assert stemmer("cake") == ("c", "ake")
    assert stemmer("chair") == ("ch", "air")
    assert stemmer("APPLE") == ("", "apple")
    assert stemmer("RDNZL") == ("rdnzl", "")


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    consonants = list("bcdfghjklmnpqrstvwxyz")
    clusters = """
bl br ch cl cr dr fl fr gl gr pl pr sc 
sh sk sl sm sn sp st sw th tr tw thw wh wr 
sch scr shr sph spl spr squ str thr""".split()
    prefixes = sorted(consonants + clusters)

    args = get_args()
    word = args.str
    start, rest = stemmer(word)

    if rest:
        print("\n".join([p + rest for p in prefixes if p != start]))
    else:
        print(f'Cannot rhyme "{word}"')


# --------------------------------------------------
if __name__ == "__main__":
    main()
