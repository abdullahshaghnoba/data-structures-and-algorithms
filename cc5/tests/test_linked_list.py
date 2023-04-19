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

##################################      cc 06 tests       ##############################
""" add a node at the end"""
def test_1():
   ll=LinkedList()
   ll.append("a")
   excepted = 'a ->  Null'
   actual = str(ll)
   assert actual == excepted
""" add multiple nodes at the end"""   
def test_2():
   ll=LinkedList()
   ll.append("a")
   ll.append("b")
   excepted = 'a -> b ->  Null'
   actual = str(ll)
   assert actual == excepted   

"""Can successfully insert a node before a node located in the middle of a linked list"""
def test_3():
   ll=LinkedList()
   ll.append("a")
   ll.append("b")
   ll.insert_before("b","v")
   excepted = 'a -> v -> b ->  Null'
   actual = str(ll)
   assert actual == excepted

"""Can successfully insert a node before the first node of a linked list"""
def test_4():
   ll=LinkedList()
   ll.append("a")
   ll.append("b")
   ll.insert_before("a","v")
   excepted = 'v -> a -> b ->  Null'
   actual = str(ll)
   assert actual == excepted

""" Can successfully insert after a node in the middle of the linked list """
def test_5():
   ll=LinkedList()
   ll.append("a")
   ll.append("b")
   ll.insert_after("a","v")
   excepted = 'a -> v -> b ->  Null'
   actual = str(ll)
   assert actual == excepted

""" Can successfully insert a node after the last node of the linked list """
def test_6():
   ll=LinkedList()
   ll.append("a")
   ll.append("b")
   ll.insert_after("b","v")
   excepted = 'a -> b -> v ->  Null'
   actual = str(ll)
   assert actual == excepted
#########################################     delete tests    ####################################
""" try to delete when the linked list is empty"""
def test_7():
    ll=LinkedList()
    excepted=False
    actual=ll.delete_node("a")
    assert actual == excepted

""" try to delete when the target is the first node in the linked list"""
def test_8():
    ll=LinkedList()
    ll.append("a")
    ll.append("b")
    ll.delete_node("a")
    excepted='b ->  Null'
    actual=str(ll)
    assert actual == excepted

""" try to delete when the target is a node in the linked list"""
def test_9():
    ll=LinkedList()
    ll.append("a")
    ll.append("b")
    ll.append("c")
    ll.delete_node("b")
    excepted='a -> c ->  Null'
    actual=str(ll)
    assert actual == excepted    

""" try to delete when the target is a node that is not in the linked list"""
def test_10():
    ll=LinkedList()
    ll.append("a")
    ll.append("b")
    ll.append("c")  
    excepted=False
    actual=ll.delete_node("e")
    assert actual == excepted
########################################## kthFromEnd tests #####################################################
"""
Where k is greater than the length of the linked list
"""

def test_11():
    ll=LinkedList()
    ll.append("a")
    ll.append("b")
    ll.append("c")  
    excepted="you are looking for a node that doesn't exist ;)"
    actual=ll.kthFromEnd(4)
    assert actual == excepted 
"""
Where k and the length of the list are the same
"""
def test_12():
    ll=LinkedList()
    ll.append("a")
    ll.append("b")
    ll.append("c")  
    excepted="you missed the head by 1 lol"
    actual=ll.kthFromEnd(3)
    assert actual == excepted
"""
Where k is not a positive integer
"""
def test_13():
    ll=LinkedList()
    ll.append("a")
    ll.append("b")
    ll.append("c")  
    excepted="out of bounds"
    actual=ll.kthFromEnd(-1)
    assert actual == excepted 
"""
Where the linked list is of a size 1
"""
def test_14():
    ll=LinkedList()
    ll.append("a")  
    excepted="a"
    actual=ll.kthFromEnd(0)
    assert actual == excepted 
"""
“Happy Path” where k is not at the end, but somewhere in the middle of the linked list
"""
def test_15():
    ll=LinkedList()
    ll.append("a")
    ll.append("b")
    ll.append("c")  
    excepted="b"
    actual=ll.kthFromEnd(1)
    assert actual == excepted               
##########################################       fixtures     ###################################################
@pytest.fixture
def ll():
    ll = LinkedList()
    ll.insert("A") 
    ll.insert("B") 
    ll.insert("C") 
    return ll