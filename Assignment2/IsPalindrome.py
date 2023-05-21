'''
Author:Grace Gong
Time Complexity: O(n)
Space Complexity: O(1)
Technique: Doubly Linked List 

Time:40 min
'''
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

def isPalindrome(head):
    left = head
    right = head

    # move right pointer to the end of the list
    while right.next is not None:
        right = right.next

    # compare the data of left and right nodes
    while left != right and left.prev != right:
        if left.data != right.data:
            return False
        left = left.next
        right = right.prev

    return True

def printList(head):
    current = head
    while current is not None:
        print(current.data, end=' ')
        current = current.next
    print()

# create a doubly linked list
head = Node(9)
head.next = Node(2)
head.next.prev = head
head.next.next = Node(4)
head.next.next.prev = head.next
head.next.next.next = Node(2)
head.next.next.next.prev = head.next.next
head.next.next.next.next = Node(9)
head.next.next.next.next.prev = head.next.next.next

# print the list
printList(head)

# check if it is a palindrome
print(isPalindrome(head))  # Output: True
