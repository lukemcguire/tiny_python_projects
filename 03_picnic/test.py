#!/usr/bin/env python3
"""tests for picnic.py"""

import os
from subprocess import getoutput

PRG = "./picnic.py"


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ["", "-h", "--help"]:
        out = getoutput(f"python3 {PRG} {flag}")
        assert out.lower().startswith("usage")


# --------------------------------------------------
def test_one():
    """one item"""

    out = getoutput(f"python3 {PRG} chips")
    assert out.strip() == "You are bringing chips."


# --------------------------------------------------
def test_two():
    """two items"""

    out = getoutput(f'python3 {PRG} soda "french fries"')
    assert out.strip() == "You are bringing soda and french fries."


# --------------------------------------------------
def test_more_than_two():
    """more than two items"""

    arg = '"potato chips" coleslaw cupcakes "French silk pie"'
    out = getoutput(f"python3 {PRG} {arg}")
    expected = "You are bringing potato chips, coleslaw, cupcakes, and French silk pie."
    assert out.strip() == expected


# --------------------------------------------------
def test_two_sorted():
    """two items sorted output"""

    out = getoutput(f"python3 {PRG} -s soda candy")
    assert out.strip() == "You are bringing candy and soda."


# --------------------------------------------------
def test_more_than_two_sorted():
    """more than two items sorted output"""

    arg = "bananas apples dates cherries"
    out = getoutput(f"python3 {PRG} {arg} --sorted")
    expected = "You are bringing apples, bananas, cherries, and dates."
    assert out.strip() == expected
