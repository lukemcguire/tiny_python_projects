#!/usr/bin/env python3
"""
Author : Luke McGuire <luke.mcguire@gmail.com>
Date   : 2024-06-29
Purpose: Southern fry text
"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Southern fry text",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", help="Input text or file")

    args = parser.parse_args()
    if os.path.isfile(args.text):
        with open(args.text, "rt", encoding="utf-8") as fh:
            args.text = fh.read().rstrip()

    return args


# --------------------------------------------------
def drop_gs(text):
    """Drop the g's from two-syllable texts ending in 'ing'"""
    pattern = re.compile(r"\b(\w*[aeiou]+\w*in)g\b", flags=re.I)
    return pattern.sub(r"\1'", text)


# --------------------------------------------------
def test_drop_gs():
    """Test drop_gs function"""
    assert drop_gs("") == ""
    assert drop_gs("sing") == "sing"
    assert drop_gs("cooking") == "cookin'"
    assert drop_gs("SINGING") == "SINGIN'"


def test_drop_gs_sentence():
    """Test drop_gs function for full lines of text"""
    text = "That's some good looking chicken."
    expected_output = "That's some good lookin' chicken."
    assert drop_gs(text) == expected_output


def test_drop_gs_first_word():
    """Test drop_gs function for first word of sentence"""
    text = "Looking good, toots."
    expected_output = "Lookin' good, toots."
    assert drop_gs(text) == expected_output


def test_drop_gs_punctuation():
    """Test drop_gs function for words followed by punctuation"""
    text = "Hey good looking, what's cooking?"
    expected_output = "Hey good lookin', what's cookin'?"
    assert drop_gs(text) == expected_output


# --------------------------------------------------
def hey_yall(text):
    """Change 'you' to 'y'all'"""
    pattern = re.compile(r"\b([yY])ou\b")
    return pattern.sub(r"\1'all", text)


# --------------------------------------------------
def test_hey_yall_one_match():
    """Test case 1: The text contains exactly one 'you'"""
    text = "You are learning Python."
    expected_output = "Y'all are learning Python."
    assert hey_yall(text) == expected_output


def test_hey_yall_no_match():
    """Test case 2: The text does not contain 'you'"""
    text = "Hello world!"
    expected_output = "Hello world!"
    assert hey_yall(text) == expected_output


def test_hey_yall_multiple_matches():
    """
    Test case 3: The text contains multiple 'you' but
    only the last one should be replaced
    """
    text = "You are so much fun. You're going to have a great time!"
    expected_output = "Y'all are so much fun. " "Y'all're going to have a great time!"
    assert hey_yall(text) == expected_output


def test_hey_yall_match_case():
    """
    Test case 4: The text contains 'You', but it should be
    replaced with 'Y'all' as the function is case-sensitive
    """
    text = "You are awesome."
    expected_output = "Y'all are awesome."
    assert hey_yall(text) == expected_output


def test_hey_yall_your():
    """Test case 5: The text contains 'your'"""
    text = "You should watch your mouth."
    expected_output = "Y'all should watch your mouth."
    assert hey_yall(text) == expected_output


def test_hey_yall_empty_string():
    """Test case 6: The input text is an empty string"""
    text = ""
    expected_output = ""
    assert hey_yall(text) == expected_output


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for line in args.text.splitlines():
        print(hey_yall(drop_gs(line)))


# --------------------------------------------------
if __name__ == "__main__":
    main()
