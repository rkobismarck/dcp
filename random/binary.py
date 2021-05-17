import math

"""
    Given an array, with a set of  numbers perform a search in 
    O(logn)
    
"""

def binary_search(arr, key):
    if len(arr) == 1:
        if arr[0] == key:
            return True
        else:
            return False
    mid     = int(math.ceil(len(arr)/2))
    value   = arr[mid] 
    if value>key:
        return binary_search(arr[0:mid], key)
    else:
        return binary_search(arr[mid:len(arr)], key) 


# Parameters to perform the search
numbers = [0,1,2,4,8,9,10,100]
key     = 4
output  = binary_search(numbers,key)
print(output)
