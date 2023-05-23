from cc17.tree_breadth_first import breadth_first
import pytest
from cc15.Node_Tree import Binary_Tree ,Node

def test_1(tree):
    actual = breadth_first(tree.root)
    expected = [-5,-10,-3,-155,-1,-4,-2]
    assert actual == expected


def test_2():
    tree = Binary_Tree()
    actual = breadth_first(tree.root)
    expected = []
    assert actual == expected

def test_3(tree1):
    actual = breadth_first(tree1.root)
    expected = [5,10,3,155,1,4,2]
    assert actual == expected






@pytest.fixture
def tree():
    tree= Binary_Tree()
    node1 = Node(-5)
    tree.root = node1
    tree.root.left=Node(-10)
    tree.root.left.left=Node(-155)
    tree.root.left.right=Node(-1)
    tree.root.right=Node(-3)
    tree.root.right.right = Node(-2)
    tree.root.right.left = Node(-4)
    return tree

@pytest.fixture
def tree1():
    tree1= Binary_Tree()
    node12 = Node(5)
    tree1.root = node12
    tree1.root.left=Node(10)
    tree1.root.left.left=Node(155)
    tree1.root.left.right=Node(1)
    tree1.root.right=Node(3)
    tree1.root.right.right = Node(2)
    tree1.root.right.left = Node(4)
    return tree1