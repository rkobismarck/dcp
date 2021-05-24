"""
    Please calculate the first n numbers of a fibonacci series.
    
    n = 8

    0,1,1,2,3,5,8,13
    

def fibonacci(n):
    print(n)
    if(n == 1):
        return 1
    if(n == 0):
        return 0
    return fibonacci(n-1) + fibonacci(n-2) 

print(fibonacci(2))
"""

def pascal_row(array):
    if len(array)==1:
        return array
    if len(array) == 2:
        return array[0]+array[1]
    else:
        arr = []
        arr.append(1)
        for index in range(0,len(array)-1):
            startIndex = index
            endIndex = index+1
            partition= array[startIndex:endIndex+1]
            arr.append(sum(partition))
        arr.append(1)
    
#print(pascal_triangle([1,1]))

def pascal_rows(n):
    for index in range(n):
        if index == 0:
            pascal_row([1])
        if index == 1:
            pascal_row([1,1])
        else:
            pascal_rows(n-1)


pascal_rows(3)