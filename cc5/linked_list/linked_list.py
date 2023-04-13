class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,value):

        node = Node(value)
        
        node.next =self.head
        self.head = node
        

    def __str__(self):

        printed_value = ""
        
        if self.head is None:
            printed_value = "Empty LinkeList"
        else:
            current = self.head
            while(current):
                printed_value += f'{current.value} -> '
                current = current.next
            
            printed_value += " Null"
        return printed_value
    
    def __repr__(self):

        printed_value = ""
        
        if self.head is None:
            printed_value = "Empty LinkeList"
        else:
            current = self.head
            while(current):
                printed_value += f'{current.value} -> '
                current = current.next
            
            printed_value += " Null"
        return printed_value
    
 
    def includes(self,key):

        temp = self.head
        # search for the key 
        while(temp):
            if temp.value == key:
                return True
            else:
               temp = temp.next
        return False
       