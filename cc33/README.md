# Code Challenge 33

---

## left_join method
        
## takes two hashmaps and left join them together in the first object
## arguments: two hashmaps
## returns: the first hashmap but left joined with the second hashmap

---

## Whiteboard Process 
[Whiteboard Process](./pics/cc33.jpg)

---

## Approach & Efficiency

---

## left_join method
## O(n) Time performance --> because we depend on the input size in the loops we use.
## O(1) Space performance --> the size of memory taken does not depend on the input size.

---

## Solution:

def left_join(H1, H2):
           
    for key in H1:
        
        if key in H2:
            H1[key] = [H1[key] , H2[key]]
        else:
            H1[key] = [H1[key], "null"]
        
    return H1