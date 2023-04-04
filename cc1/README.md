# Code Challenge: Class 01
Write a function called reverseArray which takes an array as an argument. Without utilizing any of the built-in methods available to your language, return an array with elements in reversed order.

## Whiteboard Process
[Whiteboard Process](./pics/code%20challenge%201.jpg)

## Approach & Efficiency
my code will iterate on a new array and assign the values of the given array in it from the end respectively, the Big O Time is O(n) because we only have one loop 

## Solution
def reverse_list(lst):
    arr = [0] * len(lst)
    for i in range(len(lst)):
        arr[len(lst) - i - 1] = lst[i]
    return arr 
  
my_list = [1, 2, 3, 4, 5, 6]
reverse_listed=reverse_list(my_list)
print(reverse_listed)

Output : [6,5,4,3,2,1]

## unit tests 
 def test_reverse_array(self):
        self.assertEqual(reverse_array([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
        self.assertEqual(reverse_array(["C#", "JS", "Ruby", "Python"]), ["Python", "Ruby", "JS", "C#"])
        self.assertEqual(reverse_array(["88", 10, "course", 71]), [71, "course", 10, "88"])