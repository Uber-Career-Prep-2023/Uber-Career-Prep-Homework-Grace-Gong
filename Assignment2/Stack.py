
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def top(self):
        if self.isEmpty():
            return None
        return self.top.data

    def push(self, item):
        temp = Node(item)
        temp.next = self.top
        self.top = temp

    def pop(self):
        if self.isEmpty():
            return None
        temp = self.top
        self.top = self.top.next
        return temp.data
