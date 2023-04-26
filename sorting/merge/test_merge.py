# import pytest
from merge import merge_sort

def test_merge_sort_1():
    actual = merge_sort([8,4,23,42,16,15])
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected

def test_merge_sort_2():
    actual = merge_sort([20,18,12,8,5,-2])
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected

def test_merge_sort_3():
    actual = merge_sort([5,12,7,5,5,7])
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected

def test_merge_sort_4():
    actual = merge_sort([2,3,5,7,13,11])
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected

def test_merge_sort_5():
    actual = merge_sort([2,5,7,13,11])
    expected = [2, 5, 7, 11, 13]
    assert actual == expected
