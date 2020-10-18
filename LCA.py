# Python implementation for finding the Lowest Common Ancestor in a Binary Tree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
# find path from root node to given root
def findPath(root, path, k):
    if root is None:
        return False
    
    path.append(root.key)
    if root.key is k:
        return True
    