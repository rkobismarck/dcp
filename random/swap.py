
"""
    Given an input string with a set of characters like: 
    Www.HackerRank.com → wWW.hACKERrANK.COM
    
    You'll need to transform each character.

    eg.
    Pythonist 2 → pYTHONIST 2  
    
"""


def swap(char):
    if char.isupper():
        return char.lower()
    if char.islower():
        return char.upper()
    return char


def swap_case(string):
    return ''.join([str(elem) for elem in map(swap,list(string))])


input = 'Www.HackerRank.com' 
expected ='wWW.hACKERrANK.COM'
print(swap_case(input))