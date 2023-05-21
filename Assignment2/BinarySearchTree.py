
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, node):
        if val < node.data:
            if node.left is None:
                node.left = Node(val)
            else:
                self._insert(val, node.left)
        elif val > node.data:
            if node.right is None:
                node.right = Node(val)
            else:
                self._insert(val, node.right)
        else:
            pass  # Do not handle duplicates

    def contains(self, val):
        if self.root is None:
            return False
        else:
            return self._contains(val, self.root)

    def _contains(self, val, node):
        if node is None:
            return False
        if node.data == val:
            return True
        elif val < node.data:
            return self._contains(val, node.left)
        else:
            return self._contains(val, node.right)

    def min(self):
        if self.root is None:
            return None
        else:
            return self._min(self.root)

    def _min(self, node):
        if node.left is None:
            return node.data
        else:
            return self._min(node.left)

    def max(self):
        if self.root is None:
            return None
        else:
            return self._max(self.root)

    def _max(self, node):
        if node.right is None:
            return node.data
        else:
            return self._max(node.right)

    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if node is None:
            return node
        if val < node.data:
            node.left = self._delete(node.left, val)
        elif val > node.data:
            node.right = self._delete(node.right, val)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            temp = self._min_node(node.right)
            node.data = temp.data
            node.right = self._delete(node.right, temp.data)
        return node

    def _min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
