from amsterdam import amsterdam
import pytest

def test_count():
    assert amsterdam("Am I in Amsterdam") == 1

def test_caps():
    assert amsterdam("AM AM am am lots of capital letters Am aM") == 6

def test_incorrect():
    assert amsterdam(123) == 0

def test_none():
    assert amsterdam("no things in here") == 0