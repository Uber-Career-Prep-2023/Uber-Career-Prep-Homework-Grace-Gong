'''
Author:Grace Gong
Time Complexity: O(n)
Space Complexity: O(n)
Technique: Depth-first traversal
Time:40 min
'''
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def copyTree(root):
    if root is None:
        return None
    newRoot = Node(root.data)
    newRoot.left = copyTree(root.left)
    newRoot.right = copyTree(root.right)
    return newRoot

def printTree(root):
    if root is None:
        return
    print(root.data, end=' ')
    printTree(root.left)
    printTree(root.right)

# create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# print the original tree
print("Original tree:")
printTree(root)
print()

# copy the tree and print it
newRoot = copyTree(root)
print("Copied tree:")
printTree(newRoot)
