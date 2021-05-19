
input = [1,2,3,4,5,6,7]

cache = dict()

def pow(number):
    return number * number


def get_power(number):
    if number not in cache:
        value = pow(number)
        cache[number] = value
        print('caching value')
    return cache[number]


powered = list(map(get_power, input))

print(powered)