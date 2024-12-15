import pytest

def squareAB(a, b):
    return a * a + 2 * a * b + b * b

def test_squareAB_positive_numbers():
    assert squareAB(2, 3) == 25

def test_squareAB_negative_numbers():
    assert squareAB(-2, -3) == 25