# LAB - Class 06

## Project: Linked List

### Author: Abdullah Shaghnoba
---
---
### How to run the application?
#### python  cc5/linked_list/main.py
---
### How to use your pytest library?
#### pip install -r requirements.txt
---
### How to run the tests application? 
####  **pytest**


# Code Challenge: Class 06
## Append: 
### adds a node to the end of the linked list after iterating through it 
### Arguments: value
### Returns: nothing


## Insert Before:
### adds a node before a specific node by iterating until we find it then make the node point at it and then make the prev node point at our node
### Arguments: value, new_value
### Returns: nothing


## Insert After:
### adds a node after a specific node by iterating until we find it then make the node point at it then make the current point at our node
### Arguments: value, new_value
### Returns: nothing



## Delete:
### deletes a node by searching for it's value the below function covers the cases 1)where the linked list is empty and 2) if the target
### value is the head and 3) if the target value dose not exist in the linked list the rest of the cases are included in a while loop 
### where the loop search for the value until we find it then unlink it from the link by makeing the previous node point at the next node
### Arguments: key
### Returns: True or False if the delete is done properly or not
---
## Whiteboard Process
[Whiteboard Process](./pics/cc06.jpg)

## Approach & Efficiency
for the Append method : adds a node to the end of the linked list after iterating through it.
for the Insert Before method: adds a node before a specific node by iterating until we find it then make the node point at it and then make the prev node point at our node.
for the to Insert After method: adds a node after a specific node by iterating until we find it then make the node point at it then make the current point at our node.
for the to Delete method: deletes a node by searching for it's value the below function covers the cases 1)where the linked list is empty and 2) if the target value is the head and 3) if the target value dose not exist in the linked list the rest of the cases are included in a while loop where the loop search for the value until we find it then unlink it from the link by makeing the previous node point at the next node.
Time -->O(n),for all methods. 
 
space -->O(1), since it only uses a constant amount of additional memory to keep track of the left and right indices, for all methods 

## Solution:
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