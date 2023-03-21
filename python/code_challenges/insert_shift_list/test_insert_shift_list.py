import pytest
from insert_shift_list import insert_shift_list

def test_insert_shift_list1():
    actual = insert_shift_list([2,4,6,-8], 5)
    expected = [2,4,5,6,-8]
    assert actual == expected

def test_insert_shift_list2():
    actual = insert_shift_list([42,8,15,23,42], 16)
    expected = [42,8,15,16,23,42]
    assert actual == expected

def test_insert_shift_list3():
    actual = insert_shift_list('test string', 16)
    expected = 'not a list'
    assert actual == expected

