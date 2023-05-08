import pytest

from cc11.stack_queue_pseudo import PseudoQueue

def test_1():
    ll = PseudoQueue()
    actual = ll.dequeue()
    expected = "You can't dequeue from empty stack ;)"
    assert actual == expected

def test_2():
    ll = PseudoQueue()
    ll.enqueue(1)
    actual = ll.dequeue()
    expected = 1
    assert actual == expected

def test_3():
    ll = PseudoQueue()
    ll.enqueue(1)
    ll.enqueue(2)
    actual = ll.dequeue()
    expected = 1
    assert actual == expected    

def test_4():
    ll = PseudoQueue()
    ll.enqueue(1)
    ll.enqueue(2)
    ll.dequeue()
    actual = ll.dequeue()
    expected = 2
    assert actual == expected      