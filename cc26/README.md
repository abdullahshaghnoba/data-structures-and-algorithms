# Code Challenge 26

---
## Insert function
## takes a sorted list and an input integer and places it on it's correct place
## arguments: sorted list , input integer
## returns : nothing


## InsertionSort function
## takes a list and sorts it by calling the Insert function
## arguments: list
## returns: sorted list

## breadth_first method
### Traverse a tree and returns a list withe nodes ordered by the breadth first rules
### Arguments: tree
### Return: list (nodes_in_order_bredth_first)

## Whiteboard Process 
[Whiteboard Process](./pics/code%20challenge%2026.jpg)

## Approach & Efficiency

---

## O(n^2) Time performance --> because we depend on the input size **we have to loop through the given input with a nested loop**. 
## O(n) Space performance --> the size of memory taken depends on the input size.

## Solution:

def Insert(list,value):
    i = 0
    while i < len(list) and value > list[i]:
        i += 1
    
    while i < len(list):
        temp = list[i]
        list[i] = value
        value = temp
        i += 1 
    list.append(value)



def InsertionSort(input):
    list_two = [0]
    list_two[0] = input[0]
    for i in  range(1,len(input)):
        Insert(list_two,input[i])
    return list_two