
"""
    Given an unordered array, please give one version sorted.
    You must consider time complexity algorithm.
    
    Consider writting down an quicksort algorithm.
    
"""

def sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        max = []
        min = []
        for element in arr[1:]:
            if(element>pivot):
                max.append(element)
            else:
                min.append(element)
        return sort(min) + [pivot] + sort(max)

    
arr = [10,4,5,1,300,2,50,145]
output  = sort(arr)
print(output)
