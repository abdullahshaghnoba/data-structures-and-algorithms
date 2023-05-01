# LAB - Class 08

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


# Code Challenge: Class 08
## zip_list: 
### zipps two linked lists by adding one node from each respectively  starting from linked list 1.
### Arguments: 2 linked lists.
### Return: New Linked List, zipped.
---
## Whiteboard Process
[Whiteboard Process](./pics/code%20challenge%208.jpg)

## Approach & Efficiency
### zip_list: 
### zipps two linked lists by adding one node from each respectivly starting from linked list 1
### Arguments: 2 linked lists
### Return: New Linked List, zipped.



Time -->O(n),because we have to loop through the linked list.
space -->O(1), since it only uses a constant amount of additional memory.  

## Solution:

   zipps two linked lists by adding one node from each respectivly starting from linked list 1
   Arguments: 2 linked lists
   Return: New Linked List, zipped.

---   
     
   def zip_list (self,list1,list2):
        list1_head = list1.head                 
        list2_head = list2.head 
        if list1_head == None and list2_head == None: 
            return "Both lists are empty"               
        elif list1_head == None:
            return list2             
        elif list2_head == None:
            return list1
        else:
            current = list1.head
            current_2 =list2.head
            while current and current_2  :
                if current:
                    temp = current.next
                    current.next = current_2
                    current=temp

                if current_2:
                     temp_2 = current_2.next
                     current_2.next = temp
                     current_2 = temp_2


            if current_2:
                while current_2 :
                    list1.append(current_2.value)
                    current_2=current_2.next


        return list1  