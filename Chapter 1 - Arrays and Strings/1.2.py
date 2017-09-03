# 1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other. 

def checkPermutation(string1, string2):
    counter = []
    if len(string1) != len(string2):
        return False
    for char in string1:
        counter[char] += 1
    for char in string2:
        if counter[char] == 0:
            return False
        counter[char] -= 1
    for char in counter:
        if counter[char] != 0:
            return False

    return True