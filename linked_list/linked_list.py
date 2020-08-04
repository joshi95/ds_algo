class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def printLinkedList(head):
    cur = head
    while cur != None:
        print(cur.val)
        cur = cur.next

def addElementToEndOfTheLL(head, x):
    if head is None:
        return Node(x)

    cur = head
    while cur.next != None:
        cur = cur.next
    cur.next = Node(x)
    return head

def addElementInBetweenLL(head, after_which, x):
    cur = head

    while cur.val != after_which:
        cur = cur.next
    
    new_node = Node(x)
    new_node.next = cur.next
    cur.next = new_node

    return head

if __name__ == '__main__':
    head = None # 5->15->20->25->30
    head = addElementToEndOfTheLL(head, 5)
    head = addElementToEndOfTheLL(head, 15)
    head = addElementToEndOfTheLL(head, 20)
    head = addElementToEndOfTheLL(head, 25)
    head = addElementToEndOfTheLL(head, 30)
    #printLinkedList(head)
    addElementInBetweenLL(head, 20, 100)
    printLinkedList(head)

