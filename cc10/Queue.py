from Node import Node
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def __str__(self):
        if self.front:
            queue_str = "Front -->"
            node = self.front
            while node:
              queue_str += f" {node.value} "
              node = node.next
            return queue_str    
        else:
            raise Exception("Empty Queue")

    """
    adds a new node with the given value to the back of the queue with an O(1) Time performance.
    Arguments: value
    Returns : nothing
    """
    def enqueue_queue(self,value):
        node = Node(value)

        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.size +=1    

    """
    Removes the node from the front of the queue
    Arguments: none
    Returns: the value of the removed node from the front of the queue
    Raisea exception when called on empty queue

    """

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

    """
    Gives the value of the node at the front of the queue
    Arguments: none
    Returns: Value of the node located at the front of the queue
    Raises exception when called on empty stack
    """

    def peek_queue(self):
        if not self.front:
            raise Exception("Error : This queue is empty") 
        return self.front.value    
    
    """
    Checks if the queue is empty or not
    Arguments: none
    Returns: Boolean indicating whether or not the queue is empty
    """

    def is_empty_queue(self):
        return True if self.size == 0 else False