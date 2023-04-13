import pytest
from linked_list.linked_list import LinkedList


def test_instantiate_an_empty_linked_list():
    actual =  str(LinkedList())
    expected = "Empty LinkeList"
    assert actual == expected


def test_insert():
    ll = LinkedList()
    ll.insert("A")
    actual = str(ll)
    expected = "A ->  Null"    
    assert actual == expected

def test_find_head (ll):
    actual = str(ll.head.value)
    expected = "C"    
    assert actual == expected

def test_insert_multinodes(ll):

    actual = str(ll)
    expected = "C -> B -> A ->  Null"    
    assert actual == expected

def test_search(ll):
    actual = str(ll.includes("C"))
    expected = "True"
    assert actual == expected

def test_search2(ll):
    actual = str(ll.includes("E"))
    expected = "False"
    assert actual == expected

def test_return_all_nodes(ll):

    actual = str(ll)
    expected = "C -> B -> A ->  Null"    
    assert actual == expected

@pytest.fixture
def ll():
    ll = LinkedList()
    ll.insert("A") 
    ll.insert("B") 
    ll.insert("C") 
    return ll