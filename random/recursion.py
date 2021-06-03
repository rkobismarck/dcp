"""
                        5
                4                  3
        3               2       2       1
2               1    1      0  1    0   
"""

def fibonacci(num):
    if num == 1 or num == 0:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

#print(fibonacci(7))


"""
    Hallar el primer caracter no repetido del string

    string = "aabllmmnnooppq"
"""

def non_repeated_character(string):
    for char in string:
        left  = string.index(char)
        right = string.rindex(char)
        if(left == right):
            return char


print(non_repeated_character("aabllmmnnooppq"))