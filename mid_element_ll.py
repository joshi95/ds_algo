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

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

if __name__ == '__main__':
    head = Node(10)
    head.next = Node(15)
    findMid(head)
    