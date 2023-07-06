import pytest
from cc33.left_join import left_join


def test_left_join_one():
    H1 = {'A': 1, 'B': 2}
    H2 = {'A': 1, 'C': 2}
    actual = left_join(H1 , H2)
    expected = {'A': [1,1], 'B': [2,"null"]}
    assert actual == expected

def test_left_join_two():
    H1 = {'Amjad': "1", 'Abdullah': "2"}
    H2 = {'Amjad': 1, 'C': 2}
    actual = left_join(H1 , H2)
    expected = {'Amjad': ["1",1], 'Abdullah': ["2","null"]}
    assert actual == expected

def test_left_join_three():
    H1 = {}
    H2 = {}
    actual = left_join(H1 , H2)
    expected = {}
    assert actual == expected

def test_left_join_four():
    H1 = {'Amjad': "1", 'Abdullah': "2"}
    H2 = {}
    actual = left_join(H1 , H2)
    expected = {'Amjad': ["1","null"], 'Abdullah': ["2","null"]}
    assert actual == expected

def test_left_join_five():
    H1 = {'Amjad': "1", 'Abdullah': "2"}
    H2 = {'Amjad': 9, 'Abdullah': 9}
    actual = left_join(H1 , H2)
    expected = {'Amjad': ["1",9], 'Abdullah': ["2",9]}
    assert actual == expected