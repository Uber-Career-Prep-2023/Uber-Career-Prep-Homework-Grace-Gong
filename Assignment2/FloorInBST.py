'''
Author:Grace Gong
Time Complexity: O(log n)
Space Complexity: O(1)
Technique:Search binary search tree (BST)

Time:40 min
'''
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def floorInBST(root, target):
    floor = None

    while root is not None:
        if root.data == target:
            return root.data
        elif root.data < target:
            floor = root.data
            root = root.right
        else:
            root = root.left

    return floor

# create a binary search tree
root = Node(10)
root.left = Node(8)
root.right = Node(16)
root.left.right = Node(9)
root.right.left = Node(13)
root.right.right = Node(17)
root.right.right.right = Node(20)

# print the floor in the BST for the given target
print(floorInBST(root, 13))  # Output: 13
