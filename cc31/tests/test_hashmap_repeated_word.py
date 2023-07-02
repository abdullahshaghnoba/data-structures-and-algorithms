from cc31.hashmap_repeated_word import hashmap_example

def test_hashmap_repeated_word():
    ll = hashmap_example()
    string = "Once upon a time, there was a brave princess who..."
    actual = ll.repeated_word(string)
    expected = 'a'
    assert actual == expected

def test_hashmap_repeated_word_2():
    ll = hashmap_example()
    string = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    actual = ll.repeated_word(string)
    expected = 'it'
    assert actual == expected


def test_hashmap_repeated_word3():
    ll = hashmap_example()
    string = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    actual = ll.repeated_word(string)
    expected = 'summer'
    assert actual == expected


def test_hashmap_repeated_words():
    ll = hashmap_example()
    string = "Once upon a time, there was a brave princess who..."
    string = string.lower().replace(',','')
    list_of_words = string.split()
    actual = ll.repeated_words(list_of_words)
    expected = (['a'], {'once': 1, 'upon': 1, 'a': 2, 'time': 1, 'there': 1, 'was': 1, 'brave': 1, 'princess': 1, 'who...': 1})
    assert actual == expected


def test_hashmap_repeated_words_2():
    ll = hashmap_example()
    string = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    string = string.lower().replace(',','')
    list_of_words = string.split()
    actual = ll.repeated_words(list_of_words)
    expected = (['it', 'was', 'the', 'of', 'times', 'it', 'was', 'the', 'of', 'it', 'was', 'the', 'age', 'of', 'it', 'was', 'the', 'of', 'it', 'was', 'the', 'epoch', 'of', 'it', 'was', 'the', 'of', 'it', 'was', 'the', 'season', 'of', 'it', 'was', 'the', 'of', 'it', 'was', 'the', 'of', 'we', 'had', 'before', 'us', 'we', 'we', 'were', 'all', 'going', 'direct', 'the', 'the', 'was', 'the', 'period', 'of', 'its', 'for', 'in', 'the', 'of'], {'it': 10, 'was': 11, 'the': 14, 'best': 1, 'of': 12, 'times': 2, 'worst': 1, 'age': 2, 'wisdom': 1, 'foolishness': 1, 'epoch': 2, 'belief': 1, 'incredulity': 1, 'season': 2, 'light': 1, 'darkness': 1, 'spring': 1, 'hope': 1, 'winter': 1, 'despair': 1, 'we': 4, 'had': 2, 'everything': 1, 'before': 2, 'us': 2, 'nothing': 1, 'were': 2, 'all': 2, 'going': 2, 'direct': 2, 'to': 1, 'heaven': 1, 'other': 1, 'way': 1, '–': 1, 'in': 2, 'short': 1, 'period': 2, 'so': 1, 'far': 1, 'like': 1, 'present': 1, 'that': 1, 'some': 1, 'its': 2, 'noisiest': 1, 'authorities': 1, 'insisted': 1, 'on': 1, 'being': 1, 'received': 1, 'for': 2, 'good': 1, 'or': 1, 'evil': 1, 'superlative': 1, 'degree': 1, 'comparison': 1, 'only...': 1})
    assert actual == expected


def test_hashmap_repeated_words_3():
    ll = hashmap_example()
    string = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    string = string.lower().replace(',','')
    list_of_words = string.split()
    actual = ll.repeated_words(list_of_words)
    expected = (['summer', 'the', 'i', 'was'], {'it': 1, 'was': 2, 'a': 1, 'queer': 1, 'sultry': 1, 'summer': 2, 'the': 2, 'they': 1, 'electrocuted': 1, 'rosenbergs': 1, 'and': 1, 'i': 2, 'didn’t': 1, 'know': 1, 'what': 1, 'doing': 1, 'in': 1, 'new': 1, 'york...': 1})
    assert actual == expected