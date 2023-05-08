# Code Challenge: Class 11
# PseudoQueue:
## enqueue method:
## adds a new node with the given value from a stack to the back of the queue with an O(1) Time performance.
## Arguments: value
## Returns : nothing

---
## dequeue method:
## Removes the node from the front of the queue
## Arguments: none
## Returns: the value of the removed node from the front of the queue

---

## Whiteboard Process
[Whiteboard Process](./pic/code%20challenge%2011.jpg)

---

## Approach & Efficiency
## enqueue method:
## adds a new node with the given value from a stack to the back of the queue with an O(1) Time performance.
## Arguments: value
## Returns : nothing

---

## dequeue method:
## Removes the node from the front of the queue.
## O(1) Time performance --> if first_stack and second_stack are empty
## O(n) Time performance --> if first_stack is not empty and second_stack is empty
## O(1) Time performance --> if second_stack is not empty
## Arguments: none
## Returns: the value of the removed node from the front of the queue

## Solution:

 class PseudoQueue:
    first_stack = Stack()
    second_stack = Stack()
   
    def enqueue(self,value):
        PseudoQueue.first_stack.push_stack(value)
     
    def dequeue(self):
        if PseudoQueue.first_stack.is_empty_stack() and PseudoQueue.second_stack.is_empty_stack():
            return "You can't dequeue from empty stack ;)"
        
        if PseudoQueue.second_stack.is_empty_stack() and not PseudoQueue.first_stack.is_empty_stack():
            size1 = PseudoQueue.first_stack.get_stack_size()    
            for i in range(size1):
                PseudoQueue.second_stack.push_stack(PseudoQueue.first_stack.pop_stack())
            return PseudoQueue.second_stack.pop_stack()    
        
        if not PseudoQueue.second_stack.is_empty_stack():
            return PseudoQueue.second_stack.pop_stack()