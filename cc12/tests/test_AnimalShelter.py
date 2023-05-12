import pytest
from cc12.AnimalShelter import AnimalShelter

def test_animal0():
    animal_queue = AnimalShelter()    
    animal0 = {
    "species" : "cat",
    "name" : "yummi"
    }

    animal1 = {
    "species" : "cat",
    "name" : "rengar"
    }
    animal_queue.enqueue(animal0)
    animal_queue.enqueue(animal1)
    actual = animal_queue.str()
    expected = ("Front --> {'species': 'cat', 'name': 'yummi'}  {'species': 'cat', 'name': 'rengar'} ")
    assert actual == expected

def test_animal1():
    animal_queue = AnimalShelter()    
    animal0 = {
    "species" : "cat",
    "name" : "yummi"
    }

    animal1 = {
    "species" : "cat",
    "name" : "rengar"
    }
    animal_queue.enqueue(animal0)
    animal_queue.enqueue(animal1)
    
    actual = animal_queue.dequeue("cat")
    expected = ({'name': 'yummi', 'species': 'cat'})
    assert actual == expected

def test_animal2():
    animal_queue = AnimalShelter()    
    animal0 = {
    "species" : "cat",
    "name" : "yummi"
    }

    animal1 = {
    "species" : "cat",
    "name" : "rengar"
    }
    animal_queue.enqueue(animal0)
    animal_queue.enqueue(animal1)
    animal_queue.dequeue("cat")
    animal_queue.dequeue("cat")
    actual = animal_queue.str()
    expected = ("empty queue")
    assert actual == expected

def test_animal3():
    animal_queue = AnimalShelter()    
    animal0 = {
    "species" : "cat",
    "name" : "yummi"
    }

    animal1 = {
    "species" : "cat",
    "name" : "rengar"
    }
    animal_queue.enqueue(animal0)
    animal_queue.enqueue(animal1)
    animal_queue.dequeue("cat")
    animal_queue.dequeue("cat")
    
    actual = animal_queue.dequeue("cat")
    expected = ("you can't dequeue from empty queue")
    assert actual == expected


def test_animal4():
    animal_queue = AnimalShelter()    
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
    animal_queue.enqueue(animal0)
    animal_queue.enqueue(animal1)
    animal_queue.enqueue(animal2)
    animal_queue.enqueue(animal3)
    animal_queue.dequeue("cat")
    animal_queue.dequeue("dog")
    
    actual = animal_queue.str()
    expected = ("Front --> {'species': 'dog', 'name': 'warwick'} ", "Front --> {'species': 'cat', 'name': 'rengar'} ")
    assert actual == expected


def test_animal5():
    animal_queue = AnimalShelter()    
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
    animal_queue.enqueue(animal0)
    animal_queue.enqueue(animal1)
    animal_queue.enqueue(animal2)
    animal_queue.enqueue(animal3)
    animal_queue.dequeue("cat")
    
    
    actual = animal_queue.dequeue("abcd")
    expected = ("null")
    assert actual == expected

