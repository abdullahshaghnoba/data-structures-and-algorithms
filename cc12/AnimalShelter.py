from cc10.Queue import Queue


class AnimalShelter:

    """
    creates empty queues one for cats and one for dogs 
    """
    def __init__(self):
        self.queue_cats =Queue()
        self.queue_dogs =Queue()
    """
    prints string that represents the queue
    """
    def str(self):
        if self.queue_cats.front is not None and self.queue_dogs.front is None:
            return self.queue_cats.__str__()  
        elif self.queue_cats.front is None and self.queue_dogs.front is not None:
            return self.queue_dogs.__str__() 
        elif self.queue_cats.front is None and self.queue_dogs.front is None:
            return "empty queue"
        else :
            return (self.queue_dogs.__str__()   , self.queue_cats.__str__()  )
 
    
    """
    adds a new value to the back of the queue with an O(1) Time performance.
    Arguments: animal
    Returns : nothing
    """
    def enqueue(self,animal):

        if animal["species"]=="cat":
            self.queue_cats.enqueue_queue(animal)
        if animal["species"] == "dog":
            self.queue_dogs.enqueue_queue(animal)    

    """
    Removes a value based on the given pref from the front of the queue with an O(1) Time performance
    Arguments: pref
    Returns: the removed value from the front of the queue
    """
    def dequeue(self,pref):
  
        if self.queue_cats.front==None and self.queue_dogs.front==None :
            return "you can't dequeue from empty queue"     
        if pref=="cat" and self.queue_cats.front is not None:
            return self.queue_cats.dequeue_queue()
        elif pref=="cat" and self.queue_cats.front is None:
            return "you can't dequeue from empty queue"
        elif pref=="dog"and self.queue_dogs.front is not None:
            return self.queue_dogs.dequeue_queue()
        elif pref=="dog"and self.queue_dogs.front is None:
            return "you can't dequeue from empty queue"
        else:
            return "null"    






queue = AnimalShelter()
animal0 = {
    "species" : "cat",
    "name" : "yummi"
}

animal1 = {
    "species" : "cat",
    "name" : "rengar"
}

animal2 = {
    "species" : "dog",
    "name" : "nasus"
}

animal3 = {
    "species" : "dog",
    "name" : "warwick"
}

queue.enqueue(animal0)
queue.enqueue(animal1)
queue.enqueue(animal2)
queue.enqueue(animal3)


print(queue.dequeue("cat"))
print(queue.dequeue("dog"))
print(queue.dequeue("cat"))
print(queue.dequeue("dog"))
print(queue.dequeue("abcd"))
print(queue.dequeue("dog"))
print(queue.dequeue("cat"))