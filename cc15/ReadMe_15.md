# Code Challenge 15

---
# **Binary_Tree** class
## pre_order method:
### Sorts the tree on this order (the node then it's left node then it's right node) and keeps the sorted nodes in a list.
###  Arguments: the root node in the tree.
###  return: a list that contains the sorted nodes of the tree.

## in_order method:
### Sorts the tree on this order (the left node then the node then the right node) and keeps the sorted nodes in a list.
### Arguments: the root node in the tree.
### return: a list that contains the sorted nodes of the tree.

## post_order method:
### Sorts the tree on this order (the left node then the right node then the node) and keeps the sorted nodes in a list.
### Arguments: the root node in the tree.
### return: a list that contains the sorted nodes of the tree.

# **Binary_Search_Tree** class
## Add method:
###  Adds a node in a tree in the correct position to make a binary search tree.
### Arguments: value --> the value of the node to be added
### returns nothing

## recursion method:
### helper function for the Add method to do the recursion process(search for the correct position for the node)
### Arguments: node --> the root node in the tree , value --> the value of the node to be added.
### returns nothing.

## Contains method
### searches if the tree contains a certain node.
### Arguments: value --> the value of the node we are searching for
### returns a boolean (True if the node is in the tree and False if not)

## recursive_search method
### helper function for the Contains method to do the recursion process(search for the node)
### Arguments: node --> the root node in the tree , value --> the value of the node to be searched for.
### returns boolean(True if the node is in the tree and False if not).

---

## Whiteboard Process **in_order method**
[Whiteboard Process](./pics/in_order.jpg)

## Whiteboard Process **pre_order method**
[Whiteboard Process](./pics/pre_order.jpg)

## Whiteboard Process **post_order method**
[Whiteboard Process](./pics/post_order.jpg)

## Whiteboard Process **Add method**
[Whiteboard Process](./pics/Add.jpg)

## Whiteboard Process **Contains method**
[Whiteboard Process](./pics/Contains.jpg)

---

## Approach & Efficiency

# **Binary_Tree** class
## pre_order method:
### Sorts the tree on this order (the node then it's left node then it's right node) and keeps the sorted nodes in a list.
###  Arguments: the root node in the tree.
###  return: a list that contains the sorted nodes of the tree.
## O(n) Time performance --> because we depend on the input size **we have to loop through the given Tree**. 
## O(n) Space performance --> the size of memory taken depends on the input size.

## in_order method:
### Sorts the tree on this order (the left node then the node then the right node) and keeps the sorted nodes in a list.
### Arguments: the root node in the tree.
### return: a list that contains the sorted nodes of the tree.
## O(n) Time performance --> because we depend on the input size **we have to loop through the given Tree**. 
## O(n) Space performance --> the size of memory taken depends on the input size.

## post_order method:
### Sorts the tree on this order (the left node then the right node then the node) and keeps the sorted nodes in a list.
### Arguments: the root node in the tree.
### return: a list that contains the sorted nodes of the tree.
## O(n) Time performance --> because we depend on the input size **we have to loop through the given Tree**. 
## O(n) Space performance --> the size of memory taken depends on the input size.

---

# **Binary_Search_Tree** class
## Add method:
### Adds a node in a tree in the correct position to make a binary search tree.
### Arguments: value --> the value of the node to be added
### returns nothing

## recursion method:
### helper function for the Add method to do the recursion process(search for the correct position for the node)
### Arguments: node --> the root node in the tree , value --> the value of the node to be added.
### returns nothing.

## O(log(n)) Time performance --> because we depend on the input size **we have to loop through the given Tree**. 
## O(1) Space performance --> the size of memory taken does not depend on the input size.
---

## Contains method
### searches if the tree contains a certain node.
### Arguments: value --> the value of the node we are searching for
### returns a boolean (True if the node is in the tree and False if not)

## recursive_search method
### helper function for the Contains method to do the recursion process(search for the node)
### Arguments: node --> the root node in the tree , value --> the value of the node to be searched for.
### returns boolean(True if the node is in the tree and False if not).

## O(log(n)) Time performance --> because we depend on the input size **we have to loop through the given Tree**. 
## O(1) Space performance --> the size of memory taken does not depend on the input size.

---

## Solution:

class Node:
    """
    creats a node with atributes of value,left and right
    takes a value
    returns nothing
    """
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    

#######################################################
class Binary_Tree:
    def __init__(self):
            self.root = None
    
    def pre_order(self,root,returned_list = None):
        if returned_list == None:
             returned_list=[]
        if root is not None:
            returned_list.append(root.value)
            self.pre_order(root.left,returned_list)
            self.pre_order(root.right,returned_list)
        return returned_list
    
    def in_order(self,root,returned_list=None):
        if returned_list == None:
             returned_list=[]
        if root is not None:
              self.in_order(root.left,returned_list)
              returned_list.append(root.value)
              self.in_order(root.right,returned_list)
        return returned_list
    
    def post_order(self,root,returned_list=None):
        if returned_list == None:
             returned_list=[]
        if root is not None:
              self.post_order(root.left,returned_list)
              self.post_order(root.right,returned_list)
              returned_list.append(root.value)
        return returned_list


###############################################################
class Binary_Search_Tree(Binary_Tree):
    def __init__(self):
        super().__init__()
    
    def Add(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
             self.recursion(self.root,value)
             
    def recursion(self,node,value):
            # print(node.value)
            if value > node.value:
                if node.right is None:
                    node.right = Node(value)   
                else:
                    self.recursion(node.right,value)   
            else:
                if node.left is None:
                    node.left = Node(value)   
                else:
                    self.recursion(node.left,value)

       
    def Contains(self, value):
        return self.recursive_search(self.root, value)
     
    def recursive_search(self, node, value):
        if node is None:
            return False

        if node.value == value:
            return True
        elif value < node.value:
            return self.recursive_search(node.left, value)
        else:
            return self.recursive_search(node.right, value)   
