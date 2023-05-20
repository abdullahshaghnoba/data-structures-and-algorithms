"""
duck duck goose game where you take a list and keep removing the kth element until there is only one element left and return it.
arguments :
            arr --> list
            k --> number
return :   
            the last element in the list.         
"""


arr = ["A","B","C","D","E"]
k=10
def duck_duck_goose (arr,k):
  counter = 0
  index = 0
  while len(arr) != 1:
    counter+=1
    if index == len(arr):
      index =0
    if counter == k:
      arr.pop(index)
      index-=1
      counter = 0
    index+=1
  return arr[0]
   
print(duck_duck_goose(arr,k))