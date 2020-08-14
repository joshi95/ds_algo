class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = front
        self.size = 0

    def push(self, x):
        if self.front is None:
            self.front = Node(x)
            self.rear = self.front
        else:
            self.rear.next = Node(x)
            self.rear = self.rear.next
        self.size += 1
    
    def pop(self):
        x = self.front.val
        self.front = self.front.next
        self.size -= 1
        return x
    
    def get_size(self):
        return self.size

front = Node(5)
rear = front


class DoublyLinkedListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

head = DoublyLinkedListNode(5)
node = DoublyLinkedListNode(15)
head.next = node
node.prev = head


############
# cloning a singly linked list
######

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None



def clone(head): 
    # returns a cloned linked list

    cur = head
    cloned_linked_list_head = None
    prev = None
    while cur != None:
        if cloned_linked_list_head is None:
            cloned_linked_list_head = Node(cur.val)
            prev = cloned_linked_list_head
        else:
            prev.next = Node(cur.val)
            prev = prev.next
        cur = cur.next
    return cloned_linked_list_head
            


head = Node(1)
head.next = Node(5)
head.next.next = Node(10)

new_head = clone(head)


# Leetcode 

#
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        mapping = dict()
        cur = head
        
        
        cur = head
        cloned_linked_list_head = None
        prev = None
        while cur != None:
            n = Node(cur.val)
            mapping[cur] = n
            if cloned_linked_list_head is None:
                cloned_linked_list_head = n
                prev = cloned_linked_list_head
            else:
                prev.next = n
                prev = prev.next
            cur = cur.next
            
        
        cur = head
        
        while cur != None:
            x = mapping[cur]
            if cur.random is not None:
                y = mapping[cur.random]
                x.random = y
            cur = cur.next
            
        return cloned_linked_list_head
            
        
        



