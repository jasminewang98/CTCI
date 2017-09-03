# 1.9 String Rotation:Assumeyou have a method isSubstringwhich checks if oneword is a substring
# of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
# call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat"). 

def isSubstring(string1, sub):
    return string1.find(sub) != -1

def stringRotation(s1, s2):
    if len(s1) == len(s2):
        return isSubstring(s1 + s1, s2)
    return False