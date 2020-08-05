def reverse(node):
    prev = None
    cur = node

    while cur != None:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    
    return prev

def printList(node):
    cur = node
    while cur != None:
        print(cur.val)
        cur = cur.next

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

if __name__ == '__main__':
    head = Node(10)
    head.next = Node(15)
    head.next.next = Node(20)
    #printList(head)
    new_head = reverse(head)
    printList(new_head)


    