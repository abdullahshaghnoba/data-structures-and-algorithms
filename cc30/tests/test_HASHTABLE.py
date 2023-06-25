import pytest

from cc30.HASHTABEL import HashTable

def test_hashtable_testone():
    hash_table = HashTable()
    expected = 3
    actual = len(hash_table.map)
    assert expected == actual

def test_hashtable_add_new_item():
    hash_table = HashTable()
    hash_table.set("A", 30)
    expected = ["A"]
    actual = hash_table.keys()
    assert expected == actual
    
def test_hashtable_multiple_add(test_HT):
    assert test_HT.keys() == ["N","B","A"]
    
def test_hashtable_has(test_HT):
    assert test_HT.has("A") == True
    
def test_hashtable_get(test_HT):
    assert test_HT.get("A") == 30
    
def test_hashtable_keys(test_HT):
    assert test_HT.keys() == ["N","B","A"]

@pytest.fixture
def test_HT():
    hash_table = HashTable()
    hash_table.set("A", 28)
    hash_table.set("A", 30)
    hash_table.set("N", 24)
    hash_table.set("B", 26)
    return hash_table