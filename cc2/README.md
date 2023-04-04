# Code Challenge: Class 02
Write a function which takes in an array and a value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

## Whiteboard Process
[Whiteboard Process](./pics/code%20challenge%202.jpg)

## Approach & Efficiency
the code will create an array that has the length of the given array plus 1 for the integer we are adding in the middle and will start adding the values until we reach the middle index then we will add the integer we have as an argument then we continue adding from the given array, the Big O Time is O(n) because the code has no nested stuff 

## Solution
Code : 
import math

def insertShiftArray(arr,int):

  new_arr = [0]*(len(arr)+1)
  print(new_arr)
  mid_index = len(arr)/2
  mid_index_int = math.ceil(mid_index)
  print(mid_index_int)
  for i in range(len(arr)):
    if i < mid_index_int:
      new_arr[i] = arr[i]
    elif i==mid_index_int:
      new_arr[i] = int
  for i in range(len(new_arr)):
    if i > mid_index_int:
      new_arr[i] = arr[i-1]
  return new_arr
my_array = [1, 2, 3, 4, 5]
inserted_array = insertShiftArray(my_array,10)
print(inserted_array)



Output : [1,2,3,10,4,5]

## unit tests 
 def test_insertShiftArray(self):
---
        self.assertEqual(insertShiftArray([1, 2, 3, 4, 5],10), [1,2,3,10,4,5])
---
        self.assertEqual(insertShiftArray([2,4,6,-8], 5), [2,4,5,6,-8])
---   
        self.assertEqual(insertShiftArray([42,8,15,23,42], 16), [42,8,15,16,23,42])