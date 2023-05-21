'''
Author:Grace Gong
Time Complexity: O(n) 
Space Complexity:  O(1)
Technique:Linked list fixed-distance two-pointer

Time: 40 min
'''
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def moveNthLastToFront(head, n):
    fast = slow = prev = head

    for _ in range(n):
        if fast is None:
            return None
        fast = fast.next

    while fast.next is not None:
        fast = fast.next
        prev = slow
        slow = slow.next

    prev.next = slow.next
    slow.next = head
    head = slow

    return head

def printList(head):
    current = head
    while current is not None:
        print(current.data, end=' ')
        current = current.next
    print()

head = Node(15)
head.next = Node(2)
head.next.next = Node(8)
head.next.next.next = Node(7)
head.next.next.next.next = Node(20)
head.next.next.next.next.next = Node(9)
head.next.next.next.next.next.next = Node(11)
head.next.next.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next.next.next = Node(19)

print("Original list:")
printList(head)

#indexing issue 
head = moveNthLastToFront(head, 1)
print("Updated list:")
printList(head)
