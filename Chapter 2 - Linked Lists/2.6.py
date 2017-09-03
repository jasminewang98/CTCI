# 2.6 Palindrome: Implement a function to check if a linked list is a palindrome. 

#Iterative solution with a stack
def isPalindrome(ll): #assuming no length, using a fast runner and a slow runner
   stack = []
   fast = slow = ll.head

   while fast and fast.next:
       stack.append(slow.value)
       slow = slow.next
       fast = fast.next.next

    #edge case for the last one in the half
    if fast:
        slow = slow.next
    
    while slow: 
        top = stack.pop()

        if top != slow.value:
            return False

        slow = slow.next

    return True




