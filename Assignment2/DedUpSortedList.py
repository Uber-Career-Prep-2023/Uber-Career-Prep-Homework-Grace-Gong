'''
Author:Grace Gong
Time Complexity: O(n)
Space Complexity: O(1)
Technique: simultaneous iteration two-pointer

Time: 40 min
'''
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def removeDuplicates(head):
    current = head
    while current is not None and current.next is not None:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head

def printList(head):
    current = head
    while current is not None:
        print(current.data, end=' ')
        current = current.next
    print()

# create a sorted singly linked list with duplicates
head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(5)
head.next.next.next.next.next.next = Node(5)
head.next.next.next.next.next.next.next = Node(10)
head.next.next.next.next.next.next.next.next = Node(10)

# print the original list
print("Original list:")
printList(head)

# remove duplicates and print the updated list
head = removeDuplicates(head)
print("Updated list:")
printList(head)
