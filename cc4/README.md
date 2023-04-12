# Code Challenge: Class 03
Create a function called fibonacci. The function should have one parameter n. The function should return the nth value in the fibonacci series. 
## Whiteboard Process
[Whiteboard Process](./pics/cc4.jpg)

## Approach & Efficiency
base case1 n=0 -->return 0
base case2 n= 1 -->return1
recursion
function (n) compare it with first base case, then its compare with the second base case, then the function will call it self two time with different input
for the first time n-1 and for the second time the input will be n-2, the time complexity is O(log(n)
the space complexity is O(1)
## Solution
Code : 
def fibonacci (n):
    
    # Check if input is less than 0 then it will print incorrect input
    if n < 0:
        print("Incorrect input")
    # Check if n is 0 then it will return 0
    elif n == 0:
        return 0
    # Check if n is 1 it will return 1
    elif n == 1 :
        return 1
    # the rest of the numbers goes under this case
    else:
        return fibonacci(n-1) + fibonacci(n-2)


## unit tests 
 in the tests file.
---

