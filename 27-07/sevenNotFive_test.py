import pytest
from sevenNotFive import sevenNotFive

def test_sevens():
    for i in sevenNotFive():
        assert i % 7 == 0

def test_fives():
    for i in sevenNotFive():
        assert i % 5 != 0

def test_int():
    for i in sevenNotFive():
        assert i == int(i)

def test_list():
    assert isinstance(sevenNotFive(), list) == True