class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

def insertAtFront(head, val):
    newNode = Node(val)
    newNode.next = head
    if head:
        head.prev = newNode
    return newNode

def insertAtBack(head, val):
    newNode = Node(val)
    if head is None:
        return new_node
    else:
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = newNode
        newNode.prev = curr

def insertAfter(head, val, loc):
    newNode = Node(val)
    curr = head
    while curr:
        if curr is loc:
            newNode.next = curr.next
            newNode.prev = curr
            if curr.next:
                curr.next.prev = newNode
            curr.next = newNode
            break
        curr = curr.next

def deleteFront(head):
    if head:
        newHead = head.next
        if newHead:
            newHead.prev = None
        return newHead

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
        return deleteFront(head)
    else:
        curr = head
        while curr.next:
            if curr.next is loc:
                curr.next = loc.next
                if loc.next:
                    loc.next.prev = curr
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
    curr = head
    prev = None
    while curr:
        prev = curr
        curr = curr.next
        if curr:
            curr.prev = prev
    prev.next = None
    return prev

def reverseRecursiveUtil(node):
    if node is None:
        return None
    temp = node.next
    node.next = node.prev
    node.prev = temp
    if node.prev is None:
        return node
    return reverseRecursiveUtil(node.prev)

def reverseRecursive(head):
    return reverseRecursiveUtil(head)
