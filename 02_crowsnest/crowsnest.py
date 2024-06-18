#!/usr/bin/env python3
"""
Author : Oak Hopper
Date   : 2024-06-17
Purpose: Let the captain know what you see
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Alert the captain!",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("word", metavar="word", help="The thing we see")
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word: str = args.word
    article: str = "an" if word[0].lower() in "aeiou" else "a"
    shout: str = "Ahoy, Captain, {} {} off the larboard bow!"
    print(shout.format(article.title() if word[0].isupper() else article, word))


# --------------------------------------------------
if __name__ == "__main__":
    main()
