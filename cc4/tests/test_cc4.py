import pytest

from cc4.cc4 import fibonacci

def test_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected 

def test_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected     

def test_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected     

def test_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected     

def test_four():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected   

def test_five():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected               

def test_six():
    actual = fibonacci(6)
    expected = 8
    assert actual == expected     
