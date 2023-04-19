# LAB - Class 07

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


# Code Challenge: Class 07
## kthFromEnd: 
### Searches  for a node by it's index from the end of the linked list
### Argument: a number, k, as a parameter.
### Returns the node’s value that is k places from the tail of the linked list.
    
---
## Whiteboard Process
[Whiteboard Process](./pics/code%20challenge%2007.jpg)

## Approach & Efficiency
1-I made changes on all the methods that effect the length of the linked list to add or subtract from the linked_list_length variable that I added at the start of class LinkedList
2- loop through the linked list giving each node an index and search for the node with the index that equals k from the argument and return it`s value.
3- cover the edge cases where k is not logical.

argument: a number(k) as a parameter.
Return the node’s value that is k places from the tail of the linked list.

Time -->O(n),because we have to loop through the linked list.
space -->O(1), since it only uses a constant amount of additional memory.  

## Solution:
    """
    argument: a number, k, as a parameter.
    Return the node’s value that is k places from the tail of the linked list.
    i made changes on all the methods that effect the length of the linked list to add or subtract from the linked_list_length variable
    that i added at start of class LinkedList 
    """        
    def kthFromEnd(self,k):
        length = self.linked_list_length
        print(length)
        if k>length:
            output="you are looking for a node that doesn't exist ;)" 
            return output
        elif k==length:
            output="you missed the head by 1 lol"
            return output
        elif k<int(length):
            if k<0:
                output="out of bounds"
                return output  
            node_index=length-k-1
            temp =self.head
            temp_index=0
            while temp:
                if temp_index==node_index:
                    return temp.value
                else:
                    temp=temp.next
                    temp_index+=1