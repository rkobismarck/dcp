
from typing import Dict


def is_unique(word):
    chars = dict()
    for char in word:
        if char not in chars:
            chars[char] = True
        else:
            return False
    return True

input = 'hola'
output = is_unique(input)
print(output)



