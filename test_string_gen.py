import pytest
import string
from programs.string_gen import string_gen


def test_string_gen_length():
    assert len(string_gen()) == 5

def test_string_gen_type():
    assert type(string_gen(), str)

def test_lowercase():
    assert string_gen() == string_gen().lower

def test_spaces():
    parameter = True
    word = string_gen()
    for i in word:
        if i not in string.ascii_letters:
            parameter = False
        else:
            parameter = True
    assert parameter == True
    
