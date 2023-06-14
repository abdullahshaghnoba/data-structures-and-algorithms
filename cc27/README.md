# Code Challenge 26

---

## merge_sort function 
## Takes a list and sorts it in ascending order based on the merge sort algorithm
## Arguments: list
## Returns: the sorted list

---

## merge function
## Takes three lists, left is for the left part of the main list, right is for the right part main list, arr is the main list
## Arguments: left, right, arr (all of them are lists)
## Returns: nothing

---

## Whiteboard Process 
[Whiteboard Process](./pics/code%20challenge%2027.jpg)

---

## Approach & Efficiency


### Merge Sort works by dividing the input array into two parts: a left part and a right part. Then do that recursively until we have lists of one element, Then we start the merge process by comparing the first element in each pair of lists and add the less element to the main list in the correct place and do that recursively until we have a sorted list.
---

## O(n*log(n)) Time performance --> because we depend on the input size **we have to loop through the given input with a nested loop**. 
## O(n) Space performance --> the size of memory taken depends on the input size.

## Solution:

def merge_sort(arr):
    
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        merge(left, right, arr)
    return arr

def merge(left, right, arr):
    
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    

    if i == len(left):
        arr[k:] = right[j:]
    else:
        arr[k:] = left[i:]