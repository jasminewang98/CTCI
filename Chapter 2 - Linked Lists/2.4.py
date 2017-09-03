# 2.4 Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions. 

def partition(linkedList, x):
    current = linkedList.head

    while current:
        nextNode = current.next
        current.next = None

        if current.value < x:
            current.next = head
            linkedList.head = current
        else:
            linkedList.tail.next = current
            linkedList.tail = current
        current = nextNode

    #Error check in case all nodes are less than x
    if linkedList.tail.next is not None:
        linkedList.tail.next = None