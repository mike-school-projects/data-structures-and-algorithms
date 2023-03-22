import pytest
from binary_search import binary_search

def test_binary_1():
    actual = binary_search([4, 8, 15, 16, 23, 42], 15)
    expected = 2
    assert actual == expected

def test_binary_2():
    actual = binary_search([-131, -82, 0, 27, 42, 68, 179], 42)
    expected = 4
    assert actual == expected

def test_binary_3():
    actual = binary_search([11, 22, 33, 44, 55, 66, 77], 90)
    expected = -1
    assert actual == expected
