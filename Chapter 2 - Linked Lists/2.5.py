# 2.5 Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list. 
from LinkedList import LinkedList

def addNumbers(ll1, ll2):
    current1 = ll1.head
    current2 = ll2.head
    ll = LinkedList()
    carry = 0 #value to carry over to the next digit

    while current1 or current2:
        n = current1.value + current2.value + carry
        carry = 0 #reset carryover value to 0

        if n > 10: 
            carry = n - 10
            n = n - carry
            ll.add(n)
            if current1.next == null and current2.next == null:
                ll.append(carry) #accounting for the edge case of the answer having 1 more digit than either of the added numbers

    return(ll)