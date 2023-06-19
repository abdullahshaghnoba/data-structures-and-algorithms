def merge_sort(arr):
    """
    Takes a list and sorts it in ascending order based on the merge sort algorithm
    Arguments: list
    Returns: the sorted list 
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        merge(left, right, arr)
    return arr

def merge(left, right, arr):
    """
    Takes three lists, left is for the left part of the main list, right is for the right part main list, arr is the main list
    Arguments: left, right, arr (all of them are lists)
    Returns: nothing
    """
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    

    if i == len(left):
        arr[k:] = right[j:]
    else:
        arr[k:] = left[i:]
    
    

    


arr = [10, 52, 5, 3, 8, 50, 2, 4, 9, 1, 0, 12, -1]
merge_sort(arr)
print(arr)  


    


# print(Mergesort([1,3,4,5,7,9,1]))