import pytest
from COTD_23_7 import addition

def test_int():
    assert addition("words") == "Nah that's wrong."

def test_value():
    assert addition(9) == 11106
