from cc15.Node_Tree import Node , Binary_Tree
from cc30.HASHTABEL import Hashtable
def tree_intersection(BT1, BT2):
    """
    takes two binary trees and returns the intersection values between them.
    arguments: two binary trees
    returns: list of intersection values
    """
    obj = Hashtable()
    data = Binary_Tree()
    first_tree = data.in_order(BT1)
    # print(first_tree)
    for x in first_tree:
        obj.set(x ,x)
    second_tree = data.in_order(BT2)
    return [x for x in second_tree if obj.has(x)]




if __name__ == '__main__':
    tree= Binary_Tree()
    node1 = Node(150)
    tree.root = node1
    tree.root.left=Node(100)
    tree.root.left.left=Node(75)
    tree.root.left.right=Node(160)
    tree.root.left.right.left=Node(175)
    tree.root.left.right.right=Node(125)
    tree.root.right=Node(250)
    tree.root.right.right = Node(350)
    tree.root.right.right.left = Node(300)
    tree.root.right.right.right = Node(500)
    tree.root.right.left = Node(200)
    # print(tree.find_maximum_value())
    tree2= Binary_Tree()
    node12 = Node(42)
    tree2.root = node12
    node12.left = Node(100)
    node12.right = Node(600)
    node12.left.left = Node(15)
    node12.left.right = Node(160)
    node12.left.right.left = Node(125)
    node12.left.right.right = Node(175)
    node12.right.left = Node(200)
    node12.right.right = Node(350)
    node12.right.right.left = Node(4)
    node12.right.right.right = Node(500)

    # print(tree.in_order(node1))
    # print(tree2.in_order(node12))
    # print(tree2.root.value)
    print(tree_intersection(tree.root, tree2.root))