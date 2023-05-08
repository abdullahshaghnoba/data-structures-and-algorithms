from cc10.Stack import Stack

class PseudoQueue:
    def __init__(self):
        self.first_stack = Stack()
        self.second_stack = Stack()

    """
    adds a new node with the given value from a stack to the back of the queue with an O(1) Time performance.
    Arguments: value
    Returns : nothing
    """
    def enqueue(self,value):
        self.first_stack.push_stack(value)
    """
    Removes the node from the front of the queue
    Arguments: none
    Returns: the value of the removed node from the front of the queue
    """      
    def dequeue(self):
        if self.first_stack.is_empty_stack() and self.second_stack.is_empty_stack():
            return "You can't dequeue from empty stack ;)"
        
        if self.second_stack.is_empty_stack() and not self.first_stack.is_empty_stack():
            size1 = self.first_stack.get_stack_size()    
            for i in range(size1):
                self.second_stack.push_stack(self.first_stack.pop_stack())
            return self.second_stack.pop_stack()    
        
        if not self.second_stack.is_empty_stack():
            return self.second_stack.pop_stack()


ll = PseudoQueue()
print(ll.dequeue())
ll.enqueue(1)
print(ll.dequeue())
ll.enqueue(2)
ll.enqueue(3)
print(ll.dequeue())
