# Code Challenge 32

---

## tree_intersection method
        
## takes two binary trees and returns the intersection values between them.
## arguments: two binary trees
## returns: list of intersection values

---

## Whiteboard Process 
[Whiteboard Process](./pics/cc32.jpg)

---

## Approach & Efficiency

---

## tree_intersection method
## O(n) Time performance --> bbecause we depend on the input size in the loops we use. 
## O(n) Space performance --> the size of memory taken depends on the input size.

---

## Solution:

def tree_intersection(BT1, BT2):
    
    obj = {}
    data = Binary_Tree()
    first_tree = data.in_order(BT1)
    for x in first_tree:
        obj[x] = x
    second_tree = data.in_order(BT2)
    return [x for x in second_tree if x in obj]