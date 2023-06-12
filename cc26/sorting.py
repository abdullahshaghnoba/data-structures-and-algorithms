
def Insert(list,value):
    """
takes a sorted list and an input integer and places it on it's correct place
arguments: sorted list , input integer
returns : nothing
    """
    i = 0
    while i < len(list) and value > list[i]:
        i += 1
    
    while i < len(list):
        temp = list[i]
        list[i] = value
        value = temp
        i += 1 
    list.append(value)



def InsertionSort(input):
    """
takes a list and sorts it by calling the Insert function
arguments: list
returns: sorted list
    """
    list_two = [0]
    list_two[0] = input[0]
    for i in  range(1,len(input)):
        Insert(list_two,input[i])
    return list_two

print(InsertionSort([20,18,12,8,5,-2]))
# InsertionSort()