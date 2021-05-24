"""
from functools import reduce

arr = [1,2,3,4,5,6]

def my_add(a,b):
    print(a)
    print(b)
    print('-----')
    return a+b

out= reduce(my_add,arr,0)

print(out)
"""
"""
def sequence(array):
    items = [0]
    for index in range(0, len(array)+1):
        minimum = min(array)
        if minimum not in items and minimum==items[-1]+1:
            items.append(minimum) #0(n)
            array.remove(minimum) #O(n)
        return items[1:len(items)]
""" 

def sequence(array):
    numbers = set()
    output  = set()    
    
    for  number in array: #O(n)
        numbers.add(number)

    for number in array:
        currentVal = number
        if currentVal - 1 in numbers:
            output.add(currentVal)
            output.add(currentVal-1)

    print(list(output))


print(sequence([100,4,200,1,3,2,0,6]))


