import pytest

from cc3.cc3 import BinarySearch

def test_one_BinarySearch( ):
    actual = BinarySearch([1,2,3,4,5,6,8], 3)
    expected = 2
    assert actual == expected 

def test_two_BinarySearch( ):
    actual = BinarySearch([5,10,15,20], 16)
    expected = -1
    assert actual == expected     