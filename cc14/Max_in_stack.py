from cc10.Stack import Stack

class Max_in_stack :
    def __init__(self):
        self.normal_stack = Stack()
        self.max_stack = Stack()

    def push_stack(self,value):
        self.normal_stack.push_stack(value)
        if self.max_stack.top is None:
            self.max_stack.push_stack(value)
        elif value > self.max_stack.top.value:
            self.max_stack.push_stack(value)  


    def pop_stack(self):
        return self.max_stack.pop_stack()

stack = Max_in_stack()
stack.push_stack("0")             
stack.push_stack("12")             
stack.push_stack("1234")             
stack.push_stack("123")
print(stack.normal_stack.__str__())             
print(stack.max_stack.__str__())             
print(stack.pop_stack())
print(stack.pop_stack())