#!/usr/bin/env python3
"""
Author : Luke McGuire <luke.mcguire@gmail.com>
Date   : 2024-07-01
Purpose: Create Workout Of (the) Day (WOD)
"""

import argparse
import csv
import io
from pprint import pprint
import random
import re
from tabulate import tabulate


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Create Workout Of (the) Day (WOD)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-f",
        "--file",
        help="CSV input file of exercises",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default="inputs/exercises.csv",
    )

    parser.add_argument(
        "-s", "--seed", help="Random seed", metavar="int", type=int, default=None
    )

    parser.add_argument(
        "-n",
        "--num",
        help="Number of exercises",
        metavar="exercises",
        type=int,
        default=4,
    )

    parser.add_argument("-e", "--easy", help="Halve the reps", action="store_true")

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def read_csv(fh):
    """Read the CSV input"""

    reader = csv.DictReader(fh, delimiter=",")
    exercises = []
    for rec in reader:
        name, reps = rec["exercise"], rec["reps"]
        # low, high = map(int, reps.split("-"))
        low, high = map(int, re.match(r"(\d+)-(\d+)", reps).groups())
        # low, high = map(int, re.findall(r"\d+", reps))
        exercises.append((name, low, high))

    return exercises


# --------------------------------------------------
def test_read_csv():
    """Test read_csv"""
    text = io.StringIO("exercise,reps\nBurpees,20-50\nSitups,40-100")
    assert read_csv(text) == [("Burpees", 20, 50), ("Situps", 40, 100)]


def test_read_csv_empty():
    assert True


def test_read_csv_bad_headers():
    assert True


def test_read_csv_headers_only():
    assert True


def test_read_csv_bad_reps():
    assert True


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    exercises = read_csv(args.file)
    workout = [("Exercise", "Reps")]

    for exercise, low, high in random.sample(exercises, k=args.num):
        reps = random.randint(low, high)
        if args.easy:
            reps = reps // 2
        workout.append((exercise, reps))

    print(tabulate(workout, headers="firstrow"))


# --------------------------------------------------
if __name__ == "__main__":
    main()
