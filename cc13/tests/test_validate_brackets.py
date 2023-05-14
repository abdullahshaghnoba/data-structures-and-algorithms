import pytest
from cc13.validate_brackets import validate_brackets


def test_1 ():
    assert validate_brackets("[[{}]]") == True


def test_2 ():
    assert validate_brackets("[[{}]") == False


def test_3 ():
    assert validate_brackets("aa[[{AMJAD}]aa]") == True

def test_4 ():
    assert validate_brackets("[[{())()()}]]())())(){{{()()}}}") == False

def test_5 ():
    assert validate_brackets("{}") == True

def test_6 ():
    assert validate_brackets("{}(){}") == True

def test_7 ():
    assert validate_brackets("()[[Extra Characters]]") == True

def test_8 ():
    assert validate_brackets("(){}[[]]") == True 

def test_9 ():
    assert validate_brackets("{}{Code}[Fellows](())") == True 

def test_10 ():
    assert validate_brackets("[({}]") == False 

def test_11 ():
    assert validate_brackets("(](") == False        
    
def test_12 ():
    assert validate_brackets("{(})") == False     
