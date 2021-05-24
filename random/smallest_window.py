

input = [3,7,6,5,9]

"""
    Non optimized version: this will run in 
    nlogn due to the sorting algorithm. In this case, 
    we can asume a Timsort algorithm
"""
def smallest_window(array):
    s = sorted(array)
    left_pointer, right_pointer = None, None

    for index in range(len(array)):
        if array[index] != s[index] and left_pointer is None:
            left_pointer = index
        elif array[index] != s[index]:
            right_pointer = index
    
    return (left_pointer,right_pointer)

def smalles_window_optimized(array):
    left_pointer, right_pointer = None, None
    max_seen, min_seen = -float("inf"), float("inf")

    for index in range(len(array)):
        max_seen = max(array[index], max_seen)
        if array[index] < max_seen:
            right_pointer = index 

    print(right_pointer)

    for index in range(len(array)-1,-1,-1):
        min_seen = min(array[index], min_seen)
        if array[index] > min_seen:
            left_pointer = index 
    
    print(left_pointer)

print(smalles_window_optimized(input))

