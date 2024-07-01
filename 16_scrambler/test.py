#!/usr/bin/env python3
"""tests for scrambler.py"""

import os
import re
from subprocess import getstatusoutput, getoutput

PRG = "./scrambler.py"
FOX = "../inputs/fox.txt"
BUSTLE = "../inputs/the-bustle.txt"
SPIDERS = "../inputs/spiders.txt"


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ["-h", "--help"]:
        rv, out = getstatusoutput(f"python {PRG} {flag}")
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_text1():
    """Text"""

    out = getoutput(f"python {PRG} foobar -s 1")
    assert out.strip() == "faobor"


# --------------------------------------------------
def test_text2():
    """Text"""

    text = "The quick brown fox jumps over the lazy dog."
    expected = "The qicuk bworn fox jpmus over the lzay dog."
    out = getoutput(f'python {PRG} "{text}" -s 2')
    assert out.strip() == expected


# --------------------------------------------------
def test_file_bustle():
    """File input"""

    expected = """
The blutse in a hosue
The mrinong afetr daeth
Is seosnmelt of iinuetdrss
Etecand upon etrah,--

The sweenipg up the herat,
And pniuttg lvoe away
We slahl not want to use again
Unitl eettnriy.
    """.strip()

    out = getoutput(f"python {PRG} --seed 3 {BUSTLE}")
    assert out.strip() == expected.strip()


# --------------------------------------------------
def test_file_fox():
    """File input"""

    out = getoutput(f"python {PRG} --seed 4 {FOX}")
    assert out.strip() == "The qciuk bworn fox jpums oevr the lzay dog."


# --------------------------------------------------
def test_file_spiders():
    """File input"""

    out = getoutput(f"python {PRG} --seed 9 {SPIDERS}")
    expected = "Do'nt wrory, sedrpis,\nI keep hsoue\ncalusaly."
    assert out.strip() == expected
