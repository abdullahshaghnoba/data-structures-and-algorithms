class hashmap_example:

    def __init__(self):
        self.dictionary = {}
        self.list_of_frequently_used_words = []

    def repeated_words(self, list_of_words):
        """
        Takes a list of words and returns a list of the repeted words and a dictionary of all words with the occurrences count for each word.
        Arguments: list_of_words.
        Returns: list_of_frequently_used_words, dictionary.
        """
        for word in list_of_words:
            if word in self.dictionary:
                self.dictionary[word] += 1
                self.list_of_frequently_used_words.append(word)
            else:
                self.dictionary[word] = 1
        return self.list_of_frequently_used_words , self.dictionary


    def repeated_word(self,string):
        """
        Takes a string and returns the first repeted word.
        Arguments: string.
        returns: returns the first repeted word.
        """
        string = string.lower().replace(',','')
        list_of_words = string.split()
        self.repeated_words(list_of_words)
        if self.list_of_frequently_used_words:
            return  self.list_of_frequently_used_words[0]





if __name__ == '__main__':
    # string = "Once upon a time, there was a brave princess who..."
    
    # string = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    
    string = ""
    # string = string.lower().replace(',','')
    # list_of_words = string.split()
    test = hashmap_example()
    print(test.repeated_word(string))
