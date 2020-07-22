import pytest
from COTD_22_7 import order

def test_ordering():
    assert order("a c b") == "a b c"

def test_strnumber():
    assert order("one two three 1 2 3") == "1 2 3 one three two"

def test_duplicates():    
    assert order("dupes dupes dupes dupes dupes") == "dupes"

def test_capitalisation():
    assert order("Capitalisation should NOT matter") == "Capitalisation matter NOT should"