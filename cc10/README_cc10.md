# Code Challenge: Class 10
## Stacks and Queues: 
## Stacks:
### push_stack method:
### Adds a node to the top of the stack in O(1) time complexity
### Arguments: value
### Returns: nothing

---
## pop_stack method:
### Removes the node at the top of the stack with time complexity of O(1)
### Arguments: none
### Returns : the evalue of the removed node
### Raises an exception when called on empty stack

---
## peek_stack method:
### Gives the value of the node at the top of the stack
### Arguments: none
### Returns: Value of the node located at the top of the stack
### Raises exception when called on empty stack
---
## is_empty_stack method:
### checks if the stack is empty or not
### Arguments: none
### Returns: Boolean indicating whether or not the stack is empty.
---
## Queues:
## enqueue_queue method:
### adds a new node with the given value to the back of the queue with an O(1) Time performance.
### Arguments: value
### Returns : nothing
---
## dequeue_queue method:
###  Removes the node from the front of the queue
### Arguments: none
### Returns: the value of the removed node from the front of the queue
### Raisea exception when called on empty queue
---
## peek_queue method:
###  Gives the value of the node at the front of the queue
### Arguments: none
### Returns: Value of the node located at the front of the queue
### Raises exception when called on empty stack
---
## is_empty_queue method:
### Checks if the queue is empty or not
### Arguments: none
### Returns: Boolean indicating whether or not the queue is empty

## Whiteboard Process
[Whiteboard Process](./pic/code%20challenge%2010.jpg)

## Approach & Efficiency
## Stacks:
### push_stack method:
### Adds a node to the top of the stack in O(1) time complexity
### Arguments: value
### Returns: nothing

---
## pop_stack method:
### Removes the node at the top of the stack with time complexity of O(1)
### Arguments: none
### Returns : the evalue of the removed node
### Raises an exception when called on empty stack

---
## peek_stack method:
### Gives the value of the node at the top of the stack
### Arguments: none
### Returns: Value of the node located at the top of the stack
### Raises exception when called on empty stack
---
## is_empty_stack method:
### checks if the stack is empty or not
### Arguments: none
### Returns: Boolean indicating whether or not the stack is empty.
---
## Queues:
## enqueue_queue method:
### adds a new node with the given value to the back of the queue with an O(1) Time performance.
### Arguments: value
### Returns : nothing
---
## dequeue_queue method:
###  Removes the node from the front of the queue
### Arguments: none
### Returns: the value of the removed node from the front of the queue
### Raisea exception when called on empty queue
---
## peek_queue method:
###  Gives the value of the node at the front of the queue
### Arguments: none
### Returns: Value of the node located at the front of the queue
### Raises exception when called on empty stack
---
## is_empty_queue method:
### Checks if the queue is empty or not
### Arguments: none
### Returns: Boolean indicating whether or not the queue is empty


## Time -->O(1),because our code does not depend on the size of input for all methods.
## space -->O(1), since it only uses a constant amount of additional memory for all methods.  

## Solution:

    def push_stack(self,value):
        node = Node(value)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node 
        self.size += 1      

     
    def pop_stack(self):
        if self.top:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.size -= 1
            return temp.value
        else:
            raise Exception("Error : empty stack")

    
    def peek_stack(self):
        if self.top:
            return self.top.value
        else:
            raise Exception("Error : empty stack")

 
    def is_empty_stack(self):
        return True if self.size == 0 else False
---
    def enqueue_queue(self,value):
        node = Node(value)

        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.size +=1    


    def dequeue_queue(self):

        if self.front == None:
            raise Exception("Error : This queue is empty") 

        if self.front == self.rear:
            self.rear = None

        temp = self.front
        self.front = self.front.next
        temp.next = None
        self.size -=1
        return temp.value


    def peek_queue(self):
        if not self.front:
            raise Exception("Error : This queue is empty") 
        return self.front.value    
    

    def is_empty_queue(self):
        return True if self.size == 0 else False        