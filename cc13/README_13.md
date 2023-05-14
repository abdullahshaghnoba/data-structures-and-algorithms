# Code challenge 13
---
## validate brackets function:

### Validates if the brackets are opend and closed properly in a string
### Arguments: string
### Return: boolean, representing whether or not the brackets in the string are balanced

---

## Whiteboard Process
[Whiteboard Process](./pic/code%20challenge%2013.jpg)

---

## Approach & Efficiency

### validate brackets function:

### Validates if the brackets are opend and closed properly in a string
### Arguments: string
### Return: boolean, representing whether or not the brackets in the string are balanced

## O(n) Time performance --> because we depend on the input size **we have to loop through the given string**. 
## O(k) Space performance --> the size of memory taken depends on the input size of brackets.

---

## Solution:

def validate_brackets(string):
    
    validate_stack = Stack()
    
    validate_res = True

    for i in range(len(string)):
        if string[i] == "(":
            validate_stack.push_stack(string[i])

        if string[i] == ")":
            if validate_stack.size == 0:
                return False
            x = validate_stack.pop_stack()
            if x == "(":
                validate_res = True
            else:
                validate_res = False
        if string[i] == "{":
            validate_stack.push_stack(string[i])

        if string[i] == "}":
            if validate_stack.size == 0:
                return False
            y = validate_stack.pop_stack()
            if y == "{":
                validate_res = True
            else:
                validate_res = False            
        if string[i] == "[":
            validate_stack.push_stack(string[i])

        if string[i] == "]":
            if validate_stack.size == 0:
                return False
            z = validate_stack.pop_stack()
            if z == "[":
                validate_res = True
            else:
                validate_res = False 
    if validate_stack.size != 0:
        validate_res = False        
    return validate_res