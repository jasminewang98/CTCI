# 1.5 One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away. 

def isOneAway(string1, string2):
    if len(string1) == len(string2):
        return replacedChar(string1, string2)
    else if len(string1) - len(string2) = 1:
        return insert(string1, string2)
    else if len(string2) - len(string1) = 1:
        return insert(string2, string1)
    else: 
        return False

def replacedChar(string1, string2):
    edited = False
    for i in string1:
        for j in string2:
            if string1[i] != string2[j]:
                if edited:
                    return False
                edited = True
    return True

def insertString2(string1, string2):
    edited = False
    i, j = 0, 0
    while i < len(string1) and j < len(string2):
        if string1[i] != string2[j]:
            if edited:
                return False
            edited = True
            j += 1

        else:
            i +=1
            j += 1
    return True   
