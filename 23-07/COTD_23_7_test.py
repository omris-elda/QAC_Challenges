import pytest
from COTD_23_7 import addition

def test_int():
    assert addition("words") == "Nah that's wrong."

def test_value():
    assert addition(9) == 11106

def test_multivalue():
    for i in range(0, 100):
        assert addition(i) == int(str(i + (i + (i + (i))))