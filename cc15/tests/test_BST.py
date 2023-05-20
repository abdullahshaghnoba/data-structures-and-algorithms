import pytest
from cc15.Node_Tree import Binary_Search_Tree , Binary_Tree ,Node

def test_1():
    tree= Binary_Tree()
    actual = tree.pre_order()
    expected = []
    assert actual==expected

def test_2():
    tree= Binary_Search_Tree()
    tree.Add(5)
    tree.Add(4)
    tree.Add(7)
    actual = tree.in_order(tree.root)
    expected = [4,5,7]
    assert actual==expected   

def test_3(BST):
    assert BST.pre_order(BST.root) == [5,3,2,4,7,6,8]


def test_4(BST):
    assert BST.in_order(BST.root) == [2,3,4,5,6,7,8]

def test_5(BST):
    assert BST.post_order(BST.root) == [2,4,3,6,8,7,5]    


def test_6(BST):
    assert BST.Contains(8) == True

def test_7(BST):
    assert BST.Contains(9) == False    

@pytest.fixture
def BST():
    BST= Binary_Search_Tree()
    BST.Add(5)
    BST.Add(3)
    BST.Add(2)
    BST.Add(4)
    BST.Add(7)
    BST.Add(6)
    BST.Add(8)
    return BST