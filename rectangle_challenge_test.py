import pytest
import rectangle_challenge


def test_area():
    for i in range(100):
        testrect = rectangle_challenge.Rectangle(i, i + 1)
        assert testrect.area() == i * (i + 1)

def test_int():
    for i in range(100):
        testrect = rectangle_challenge.Rectangle(i, i + 1)
        assert isinstance(testrect.area(), int) == True

