# function should return index to the any valid peak element
def findMid(head):
    # Code here
    # return the value stored in the middle node
    fp = head
    sp = head
    
    while sp != None and fp != None and fp.next != None:
        sp = sp.next
        fp = fp.next.next
    
    return sp.data
