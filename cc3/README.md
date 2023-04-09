# Code Challenge: Class 03
Write a function which takes in an array and a value. Without utilizing any of the built-in methods available to your language, return the index of the value if available or return -1, follow the binary search algorithm.

## Whiteboard Process
[Whiteboard Process](./pics/code%20challenge%203%20(1).jpg)

## Approach & Efficiency
the code will compare the key with middle item in the list if they are equal, it will return the index if not, will see if it is bigger it will search the right half of the list if it is less it will search the left half of the list by comparing the key with middle item of that part of list each time, if the key is not in the list the code will return -1, the Big O Time is O(Log n) since it divides the search range in half at each iteration , space -->O(1), since it only uses a constant amount of additional memory to keep track of the left and right indices.

## Solution
Code : 
def BinarySearch(arr, key):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return -1

## unit tests 
 def test_BinarySearch(self):
---
        self.assertEqual(BinarySearch([1, 2, 3, 4, 5, 6,7],5), 4)
---
        self.assertEqual(BinarySearch([1, 2, 3, 4, 5, 6,7],8), -1)
