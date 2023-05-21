'''
Author:Grace Gong
Time Complexity: O(n)
Space Complexity: O(n)
Technique: Level-order (breadth-first) traversal

Time: 40 min
'''
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def leftView(root):
    if root is None:
        return []
    
    result = []
    queue = [root]

    while queue:
        levelSize = len(queue)
        for i in range(levelSize):
            node = queue.pop(0)
            if i == 0:
                result.append(node.data)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
    
    return result

# create a binary tree
root = Node(7)
root.left = Node(8)
root.right = Node(3)
root.right.left = Node(9)
root.right.right = Node(13)
root.right.left.left = Node(20)
root.right.right.left = Node(14)
root.right.right.left.right = Node(15)

# print the left view of the tree
print(leftView(root))  # Output: [7,8,9,20,15]
