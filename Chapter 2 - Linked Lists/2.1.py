#2.1 Remove Dups! Write code to remove duplicates from an unsorted linked list. 
from LinkedList import LinkedList

#uses an array for seen values
def removeDups(linkedList):
    if linkedList.head is None:
        return

    current = linkedList.head
    seen = set([current.value])
    while current.next != none:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            current = current.next
    return linkedList

#uses a runner to avoid using a separate array

def removeDupsFollowup(linkedList):
    if linkedList.head is None:
        return

    current = linkedList.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

    return linkedList.head
