# Code Challenge: Class 12
# AnimalShelter:
## enqueue method:
## adds a new value to the back of the queue with an O(1) Time performance.
##  Arguments: animal
##  Returns : nothing
---
## dequeue method:
## Removes a value based on the given pref from the front of the queue
##  Arguments: pref
##  Returns: the removed value from the front of the queue

---

## Whiteboard Process
[Whiteboard Process](./pic/code%20challenge%2012.jpg)

---

## Approach & Efficiency
## enqueue method:
## adds a new value to the back of the queue with an O(1) Time performance.
##  Arguments: animal
##  Returns : nothing

## dequeue method:
## Removes a value based on the given pref from the front of the queue
##  Arguments: pref
##  Returns: the removed value from the front of the queue

## O(1) Time performance --> for enqueue method because we don't depend on the input size
## O(1) Time performance --> for dequeue method because we don't depend on the input size
## O(n) Space performance --> the size of memory taken depend on the input size
## Solution:

 class AnimalShelter:

    """
    creates empty lists one for cats and one for dogs 
    """
    def __init__(self):
        self.queue_cats =[]
        self.queue_dogs =[]
    """
    prints string that represents the queue
    """
    def str(self):
        if len(self.queue_cats)!=0 and len(self.queue_dogs)==0:
            return self.queue_cats  
        elif len(self.queue_cats)==0 and len(self.queue_dogs)!=0 :
            return self.queue_dogs
        elif len(self.queue_cats)==0 and len(self.queue_dogs)==0 :
            return "empty queue"
        else :
            return (self.queue_dogs  , self.queue_cats )
 
    
    """
    adds a new value to the back of the queue with an O(1) Time performance.
    Arguments: animal
    Returns : nothing
    """
    def enqueue(self,animal):

        if animal["species"]=="cat":
            self.queue_cats.append(animal)
        if animal["species"] == "dog":
            self.queue_dogs.append(animal)    

    """
    Removes a value based on the given pref from the front of the queue
    Arguments: pref
    Returns: the removed value from the front of the queue
    """
    def dequeue(self,pref):
        if len(self.queue_cats)==0:
            if len(self.queue_dogs)==0:
                return "you can't dequeue from empty queue"
            return "you can't dequeue from empty queue"        
        if pref=="cat":
            return self.queue_cats.pop(0)
        elif pref=="dog":
            return self.queue_dogs.pop(0)
        else:
            return "null"    
