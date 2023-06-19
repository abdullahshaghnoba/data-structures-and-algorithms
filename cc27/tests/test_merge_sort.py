import pytest
from cc27.merge_sort import merge_sort

def test_1():
    actual = merge_sort([1,5,6,7,9,4,3])
    expected = [1,3,4,5,6,7,9]
    assert actual == expected


def test_2():
    
    actual = merge_sort([5, 2, 8, 3, 1]) 
    expected = [1, 2, 3, 5,8]
    assert actual == expected

def test_3():
    
    actual = merge_sort([9,8,7,6,5,4,3,2,1]) 
    expected = [1,2,3,4,5,6,7,8,9]
    assert actual == expected

def test_4():
    
    actual = merge_sort([20,18,12,8,5,-2]) 
    expected = [-2,5,8,12,18,20]
    assert actual == expected

def test_5():
    
    actual = merge_sort([5,12,7,5,5,7]) 
    expected = [5,5,5,7,7,12]
    assert actual == expected

def test_6():
    
    actual = merge_sort([2,3,5,7,13,11]) 
    expected = [2,3,5,7,11,13]
    assert actual == expected