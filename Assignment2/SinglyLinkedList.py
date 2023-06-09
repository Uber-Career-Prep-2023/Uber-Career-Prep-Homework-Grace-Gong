
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def insertAtFront(head, val):
    new_node = Node(val)
    new_node.next = head
    return new_node

def insertAtBack(head, val):
    new_node = Node(val)
    if head is None:
        return new_node
    else:
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = new_node

def insertAfter(head, val, loc):
    new_node = Node(val)
    curr = head
    while curr:
        if curr is loc:
            new_node.next = curr.next
            curr.next = new_node
            break
        curr = curr.next

def deleteFront(head):
    if head:
        return head.next

def deleteBack(head):
    if head:
        if head.next is None:
            return None
        else:
            curr = head
            while curr.next.next:
                curr = curr.next
            curr.next = None
    return head

def deleteNode(head, loc):
    if head is loc:
        return head.next
    else:
        curr = head
        while curr.next:
            if curr.next is loc:
                curr.next = loc.next
                break
            curr = curr.next
    return head

def length(head):
    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next
    return count

def reverseIterative(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def reverseRecursiveUtil(curr, prev):
    if curr.next is None:
        curr.next = prev
        return curr
    next_node = curr.next
    curr.next = prev
    return reverseRecursiveUtil(next_node, curr)

def reverseRecursive(head):
    if head is None:
        return head
    return reverseRecursiveUtil(head, None)