# 1.1: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures? 

#Assumes ASCII character set
#uses additional data structures

#Solution 1 with time compleixty of O(n)
def unique(string):
    if string.length() > 256 return False #extended ASCII

    char_set = [False for i in range(string.length)]
    for char in string:
        #returns an integer representing the unicode code point of the character when the argument is a unicode object
        val = ord(char) 
        if char_set[val]:
            #Char already found in string
            return False
        char_set[val] = True

    return True

#TODO: Solution 2 (requires bit manipulation which I don't know yet)