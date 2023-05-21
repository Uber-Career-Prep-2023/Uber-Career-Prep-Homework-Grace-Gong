'''
Author:Grace Gong 
Time Complexity: O(n)
Space Complexity: O(1)
Technique: Linked list fast-slow two-pointer

Time: 40 min
'''
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def disconnectCycle(head):
    fast = slow = head

    # find the meeting point inside the cycle
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    # check if there's no cycle
    if fast is None or fast.next is None:
        return None

    # find the start node of the cycle
    slow = head
    while slow != fast:
        slow = slow.next
        prev = fast
        fast = fast.next

    # disconnect the cycle
    prev.next = None

def printList(head):
    current = head
    while current is not None:
        print(current.data, end=' ')
        current = current.next
    print()

# create a singly linked list with a cycle
head = Node(10)
head.next = Node(18)
head.next.next = Node(12)
head.next.next.next = Node(9)
head.next.next.next.next = Node(11)
head.next.next.next.next.next = Node(4)
head.next.next.next.next.next.next = head.next.next.next  # create a cycle

# disconnect the cycle
disconnectCycle(head)

# print the list after disconnecting the cycle
printList(head)  # Output: 10 18 12 9 11 4
