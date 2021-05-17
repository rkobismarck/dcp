"""
    Please calculate the first n numbers of a fibonacci series.
    
    n = 8

    0,1,1,2,3,5,8,13
    
"""

def fibonacci(n):
    if(n == 1):
        return 1
    if(n == 0):
        return 0
    return fibonacci(n-1) + fibonacci(n-2) 

print(fibonacci(7))