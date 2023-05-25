from cc15.Node_Tree import Binary_Tree , Node
from cc10.Queue import Queue

"""
Traverse a tree and returns a list withe nodes ordered by the breadth first rules
Arguments: tree
Return: list (nodes_in_order_bredth_first)
"""
def breadth_first(tree):
    if not tree:
        return []
    queue = Queue()
    queue.enqueue_queue(tree)

    nodes_in_order_bredth_first = []

    while queue.front:
        node = queue.dequeue_queue()

        nodes_in_order_bredth_first.append(node.value)

        if node.left:
            queue.enqueue_queue(node.left)

        if node.right:
            queue.enqueue_queue(node.right)

    return nodes_in_order_bredth_first



if __name__=="__main__":
    tree = Binary_Tree()
    tree.root = Node(5)
    tree.root.left = Node(8)
    tree.root.left.left= Node(10)
    tree.root.right = Node(15)
    tree.root.right.right = Node(1)
    print(breadth_first(tree.root))