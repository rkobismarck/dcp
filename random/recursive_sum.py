"""
    Given an array, with a numbers please perform the sum of all'em 
    
    Hint: Consider using recursive approach for this specific case.
    
"""
def sum(numbers):
    if len(numbers) == 0:
        return None
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + sum(numbers[1:len(numbers)])

input  = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output = sum(input)
print(output)