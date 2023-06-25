# Code Challenge 30

---

## hash method
        
## takes a key and returns the hashed value of the key as the index
## Args:key
## returns the index
---

## set method

## takes a key and a value and adds the key value pair to the hash table
## args:key , value
## returns nothing

---

## has method
       
## takes a key and returns True if the key exists in the hash table and False otherwise
## args: key
## returns True or False

---

## keys method
        
## takes no arguments and returns a list of keys in the hash table
## args: none
## returns a list of keys

---

## get method
        
## takes a key and returns the value associated with the key
## args: key
## returns the value associated with the key

---

## Approach & Efficiency

---

## hash method
## O(n) Time performance --> because we depend on the input size **we have to loop through the given input **. 
## O(1) Space performance --> the size of memory taken does not depend on the input size.

---

## set method
## O(n) Time performance --> because we depend on the input size **we have to loop through the given input **. 
## O(n) Space performance --> the size of memory taken depends on the input size.

---

## has method
## O(n) Time performance --> because we depend on the input size **we have to loop through the given input **. 
## O(1) Space performance --> the size of memory taken does not depend on the input size.

---

## keys method
## O(n) Time performance --> because we depend on the input size **we have to loop through the given input **. 
## O(n) Space performance --> the size of memory taken depends on the input size.

---

## get method
## O(n) Time performance --> because we depend on the input size **we have to loop through the given input **. 
## O(1) Space performance --> the size of memory taken does not depend on the input size.

---
## Solution:

class HashTable():
    def __init__(self,size=3):
        self.size = size
        self.map = [None]*size

    def hash(self, key):
        
        sum_of_asccii = 0
        for ch in key:
            asccii_of_ch = ord(ch)
            sum_of_asccii += asccii_of_ch
        temp = sum_of_asccii*599
        indx = temp%self.size
        return indx
    
    def set(self, key, value):
        
        index = self.hash(key)
        if not self.map[index]: 
            self.map[index] = [key,value]
        else: 

            if key == self.map[index][0]:
                exsiting_pair = self.map[index]
                exsiting_pair[1] = value
            else:
                exsiting_pair = self.map[index]
                new_pair = [key, value]
                self.map[index] = []
                self.map[index].append(exsiting_pair)
                value_flag = True
                for x in self.map[index]:
                    print(x[0])
                    if key == x[0]:
                        value_flag = False
                        x[1] = value
                if value_flag:   
                    self.map[index].append(new_pair) 

    def has(self , key ):
        
        for x in self.map:
            if len(x[0]) > 1:
                for y in x:
                    if key == y[0]:
                        return True
            else:
                if key == x[0]:
                       return True
        return False

    def keys(self):
        
        keys = []
        for x in self.map:
            if x is None:
                pass
            else:
                if len(x[0]) > 1:
                    for y in x:
                        keys.append(y[0])
                else:
                    keys.append(x[0])
        return keys
        
    
    def get(self , key):
        
        if self.has(key):
            index = self.hash(key)
            if len(self.map[index][0]) > 1:
                for x in self.map[index]:
                    if key == x[0]:
                        return x[1]
            else:
                return self.map[index][1]