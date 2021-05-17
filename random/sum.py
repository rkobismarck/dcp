from collections import Counter

"""
    Given an array input with n numbers, and a parameter x:

    Please find a tuple of numbers that added are equal to x, if possible
    inside the array.

    Please consider a brtue force solution, and improve this into a
    better one.
"""

def find_tuple(arr, sum):
    numbers = dict()
    numbers = Counter(arr)
    items = []
    
    for element in arr:
        residual = sum - element
        if(residual in numbers):
            items.append([residual, element])
            break

    return items

arr = [1,2,4,9,18,60]
sum = 13
output  = find_tuple(arr,sum)
print(output)
