# Code Challenge 17

---

## breadth_first method
### Traverse a tree and returns a list withe nodes ordered by the breadth first rules
### Arguments: tree
### Return: list (nodes_in_order_bredth_first)

## Whiteboard Process **in_order method**
[Whiteboard Process](./pics/breadth_first%20.jpg)

## Approach & Efficiency

---

## breadth_first method
### Traverse a tree and returns a list withe nodes ordered by the breadth first rules
### Arguments: tree
### Return: list (nodes_in_order_bredth_first)

## O(n) Time performance --> because we depend on the input size **we have to loop through the given Tree**. 
## O(n) Space performance --> the size of memory taken depends on the input size.

## Solution:

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