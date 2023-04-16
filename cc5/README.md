# LAB - Class 05

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


# Code Challenge: Class 05
insert
Arguments: value
Returns: nothing
Adds a new node with that value to the head of the list with an O(1) Time performance.
includes
Arguments: value
Returns: Boolean
Indicates whether that value exists as a Node’s value somewhere within the list.
to string
Arguments: none
Returns: a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"
## Whiteboard Process
[Whiteboard Process](./pics/cc%205%20whiteboard.png)

## Approach & Efficiency
for the insert method : the way is to create a node then make it point on the head then make it the head.
for the includes method: the way is to traverse along the linked list and search for a node and return true if exists or false if not.
for the to string method: the idea is to print the whole linked list.
Time -->O(1),for the insert method 
Time -->O(n),for the includes method
Time -->O(n),for the insert method  
space -->O(1), since it only uses a constant amount of additional memory to keep track of the left and right indices, for all methods 
## Solution
Code : 
 def insert(self,value):

        node = Node(value)
        
        node.next =self.head
        self.head = node
        
----
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
----
def includes(self,key):

        temp = self.head
        # search for the key 
        while(temp):
            if temp.value == key:
                return True
            else:
               temp = temp.next
        return False

## unit tests 
 in the tests file.
---
