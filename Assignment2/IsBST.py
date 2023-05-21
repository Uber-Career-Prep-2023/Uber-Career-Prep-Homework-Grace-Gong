'''
Author:Grace Gong
Time Complexity: O(n)
Space Complexity: O(n)
Technique: Depth-first traversal

Time: 40 min
'''
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def isBST(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True

    if not min_val <= root.data < max_val:
        return False

    return isBST(root.left, min_val, root.data) and isBST(root.right, root.data, max_val)

# create a binary search tree
root = Node(10)
root.left = Node(8)
root.right = Node(16)
root.left.right = Node(9)
root.right.left=Node(13)
root.right.right=Node(17)
root.right.right.right=Node(20)

# check if it is a BST
print(isBST(root))  # Output: True

# create a binary tree which is not a BST
root = Node(10)
root.left = Node(8)
root.right = Node(16)
root.left.right = Node(9)
root.right.left=Node(13)
root.right.right=Node(17)
root.right.right.right=Node(15)

# check if it is a BST
print(isBST(root))  # Output: False
