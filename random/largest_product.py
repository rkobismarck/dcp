"""
    Given an array if integers, return a new array such that each element at index i of
    the new array is the product of all the numbers in the original array except the one
    at i.

    For example if our input was [1, 2, 3, 4, 5], the expected output would be [120, 
    60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

    Let's say that the original array will be:

    nums = [1, 2, 3, 4, 5]

    So if we take a look, we can partition by right and left the origina array.

    nums[0] = left[-1] - right[1:len(nums)] 
    nums[1] = left[1]

"""
input = [1,5,4,2]

def largest_product(nums):
    preffix = []
    suffix  = []
    for num in nums:
        if len(preffix) == 0:
            preffix.append(num)
        else:
            preffix.append(preffix[-1]*num)

    for num in reversed(nums):
        if len(suffix) == 0:
            suffix.append(num)
        else:
            suffix.append(suffix[-1]*num)

    suffix = list(reversed(suffix))
    
    results = []

    for num in range(len(nums)):
        if num == 0:
            results.append(suffix[num+1])
        elif num == len(nums)-1:
            results.append(preffix[num-1])
        else:
            results.append(suffix[num+1]*preffix[num-1])

    return results
    
print(largest_product(input))