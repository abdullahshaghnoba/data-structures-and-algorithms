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
    """
    adds a node to the end of the linked list after iterating through it 
    """
    def append(self,value):
        node = Node(value)
        if self.head is None:
            self.head=node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
    """
    adds a node before a specific node by iterating until we find it then make the node point at it and then make the prev node point at our node
    """
    def insert_before(self, value, new_value):
       node = Node(new_value)
       if self.head == None:
        self.head = node
       else:
         current = self.head
         prev = None
         while current:
            if current.value == value:
                node.next = current
                if prev:
                    prev.next = node
                else:
                    self.head = node
                return
            prev = current
            current = current.next
    """
    adds a node after a specific node by iterating until we find it then make the node point at it then make the current point at our node
    """
    def insert_after(self,value,new_value):
        node = Node(new_value)
        if self.head == None:
            self.head = node
        else:                
            current=self.head
            while current:
                if current.value==value:
                    node.next=current.next
                    current.next=node
                current=current.next    
    """
    deletes a node by searching for it's value the below function covers the cases 1)where the linked list is empty and 2) if the target
    value is the head and 3) if the target value dose not exist in the linked list the rest of the cases are included in a while loop 
    where the loop search for the value until we find it then unlink it from the link by makeing the previous node point at the next node
    """
    def delete_node(self,key):

        temp = self.head

        # 1. Empty linked list
        if (temp is None):
            return False
        
        # 2. If the target is the first node
        if (temp is not None):
            if(temp.value == key):
                self.head = temp.next
                temp = None
                return 
            
        # search for the key and delete the target node
        while(temp is not None):
            if temp.value == key:
                break
            prev = temp
            temp = temp.next

        # 3. The key does not Exists
        if(temp is None):
            return False

        # unlink the target node from the linkedlist
        prev.next = temp.next
        temp = None
        return True
            
                
       