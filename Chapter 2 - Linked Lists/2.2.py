# 2.2 Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list. 

def kthToLast(linkedList, k):
    runner = current = linkedList.head
    for i in range(k):
        if runner is None:
            return None
        runner = runner.next
    
    while runner:
        current = current.next
        runner = runner.next
    
    return current
