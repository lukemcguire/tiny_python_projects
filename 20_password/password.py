#!/usr/bin/env python3
"""
Author : Luke McGuire <luke.mcguire@gmail.com>
Date   : 2024-07-02
Purpose: Password maker
"""

import argparse
import random
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Password maker",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file",
        help="Input file(s)",
        metavar="FILE",
        type=argparse.FileType("rt"),
        nargs="+",
    )

    parser.add_argument(
        "-n",
        "--num",
        help="Number of passwords to generate",
        metavar="int",
        type=int,
        default=3,
    )

    parser.add_argument(
        "-w",
        "--num_words",
        help="Number of words per password",
        metavar="int",
        type=int,
        default=4,
    )

    parser.add_argument(
        "-m",
        "--min_word_len",
        help="Minimum length of word",
        metavar="int",
        type=int,
        default=3,
    )

    parser.add_argument(
        "-x",
        "--max_word_len",
        help="Maximum length of word",
        metavar="int",
        type=int,
        default=6,
    )

    parser.add_argument(
        "-s", "--seed", help="Seed for random", metavar="int", type=int, default=None
    )

    parser.add_argument(
        "-l", "--l33t", help="Obfuscate the password", action="store_true"
    )

    return parser.parse_args()


# --------------------------------------------------
def choose(char: str) -> str:
    """Choose a random case for a character"""

    return random.choice([char.lower(), char.upper()])


# --------------------------------------------------
def test_choose():
    """Test choose"""

    state = random.getstate()
    random.seed(1)
    assert choose("a") == "a"
    assert choose("b") == "b"
    assert choose("c") == "C"
    assert choose("d") == "d"
    random.setstate(state)


# --------------------------------------------------
def ransom(passwd: str) -> str:
    """Randomly capitalize and lowercase letters ala a ransom note"""

    return "".join(map(choose, passwd))


# --------------------------------------------------
def test_ransom():
    """Test ransom function"""

    state = random.getstate()
    random.seed(1)
    assert ransom("Money") == "moNeY"
    assert ransom("Dollars") == "DOLlaRs"
    random.setstate(state)


# --------------------------------------------------
def l33t(passwd: str) -> str:
    """Obfuscate the password using l33t rules"""
    l33t_table = {"a": "@", "A": "4", "O": "0", "t": "+", "E": "3", "I": "1", "S": "5"}
    ransom_note = ransom(passwd)
    l33ted = ransom_note.translate(str.maketrans(l33t_table))
    return l33ted + random.choice(string.punctuation)


# --------------------------------------------------
def test_l33t():
    """Test l33t function"""

    state = random.getstate()
    random.seed(1)
    assert l33t("Money") == "moNeY{"
    assert l33t("Dollars") == "D0ll4r5`"
    random.setstate(state)


# --------------------------------------------------
def clean(word):
    """Remove non-alphanumeric characters fro word"""

    return "".join(filter(str.isalpha, word))


# --------------------------------------------------
def test_clean():
    """Test clean function"""

    assert clean("") == ""
    assert clean("states,") == "states"
    assert clean("Don't") == "Dont"


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    words = set()

    def word_len(word):
        """filter words list to match length requirements"""
        return args.min_word_len <= len(word) <= args.max_word_len

    for fh in args.file:
        for line in fh:
            for word in filter(word_len, map(clean, line.title().split())):
                words.add(word)

    words = sorted(words)
    passwords = ["".join(random.sample(words, args.num_words)) for _ in range(args.num)]

    for passwd in passwords:
        if args.l33t:
            passwd = l33t(passwd)
        print(passwd)


# --------------------------------------------------
if __name__ == "__main__":
    main()
