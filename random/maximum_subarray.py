def maximum_subarray_sum(numbers):
    acc = 0 
    stop_position = len(numbers)-1

    for currentIndex in range(len(numbers)):
        currentValue    = numbers[currentIndex]
        temp            = acc + currentValue
        if temp < 0:
            acc = 0
        else:
            if currentIndex == stop_position and currentValue<0:
                continue
            else:
                acc = acc + currentValue
    return acc

input = [34, -50, 42, 14,-5, 86]
print(maximum_subarray_sum(input))