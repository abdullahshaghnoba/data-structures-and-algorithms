from Node import Node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0


    def __str__(self):
        if self.top:
            stack_str = "Top -->"
            node = self.top
            while node:
              stack_str += f" {node.value} "
              node = node.next
            return stack_str    
        else:
            raise Exception("Empty Queue")


    """
    Adds a node to the top of the stack in O(1) time complexity
    Arguments: value
    Returns: nothing

    """
    def push_stack(self,value):
        node = Node(value)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node 
        self.size += 1      

    """
    Removes the node at the top of the stack with time complexity of O(1)
    Arguments: none
    Returns : the evalue of the removed node
    Raises an exception when called on empty stack

    """   
    def pop_stack(self):
        if self.top:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.size -= 1
            return temp.value
        else:
            raise Exception("Error : empty stack")

    """
    Gives the value of the node at the top of the stack
    Arguments: none
    Returns: Value of the node located at the top of the stack
    Raises exception when called on empty stack
    """    
    def peek_stack(self):
        if self.top:
            return self.top.value
        else:
            raise Exception("Error : empty stack")

    """
    checks if the stack is empty or not
    Arguments: none
    Returns: Boolean indicating whether or not the stack is empty.
    """   
    def is_empty_stack(self):
        return True if self.size == 0 else False