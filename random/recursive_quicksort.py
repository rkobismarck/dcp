"""
    Given an array with non sorted values, please implement a method whose main
    purpose will be returning an array with ordered numbers.

    Hint: Please consider using some recursion, and implement an algorithm with 
    complexity O (n*logn)
    
"""


input       = [6,1,4,3,9,15,100,5,2,58,96]


def quicksort(array):
    if len(array)<2:
        return array
    else:
        left_partition  = []
        right_partition = []
        pivot           = array[0]
        
        for index in range(1,len(array)):
            current_value   = array[index]
            if current_value <= pivot:
                left_partition.append(current_value) 
            else:
                right_partition.append(current_value)
    return quicksort(left_partition) + [pivot] + quicksort(right_partition)

output = quicksort(input)
print(output)