# Code Challenge 31

---

## repeated_word method
        
## Takes a string and returns the first repeted word.
## Arguments: string.
## returns: returns the first repeted word.
---

## repeated_words method

## Takes a list of words and returns a list of the repeted words and a dictionary of all words with the occurrences count for each word.
## Arguments: list_of_words.
## Returns: list_of_frequently_used_words, dictionary.

---

## Whiteboard Process 
[Whiteboard Process](./pics/cc31.jpg)

---

## Approach & Efficiency

---

## repeated_word method
## O(n^2) Time performance --> because the replace() method depends on the length of the input string. In the worst case, when the target substring (',') occurs at every position. 
## O(n) Space performance --> the size of memory taken does depends on the input size.

---

## repeated_words method
## O(n) Time performance --> because we depend on the input size **we have to loop through the given input **. 
## O(n) Space performance --> the size of memory taken depends on the input size.

---

## Solution:

class hashmap_example:

    def __init__(self):
        self.dictionary = {}
        self.list_of_frequently_used_words = []

    def repeated_words(self, list_of_words):
        
        for word in list_of_words:
            if word in self.dictionary:
                self.dictionary[word] += 1
                self.list_of_frequently_used_words.append(word)
            else:
                self.dictionary[word] = 1
        return self.list_of_frequently_used_words , self.dictionary


    def repeated_word(self,string):
        
        string = string.lower().replace(',','')
        list_of_words = string.split()
        self.repeated_words(list_of_words)

        if self.list_of_frequently_used_words:
            return  self.list_of_frequently_used_words[0]