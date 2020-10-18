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

def findLCA(root, nr1, nr2):
    path1 = []
    path2 = []

    # find path1 and path2 from root and return -1 if either node is not present
    if (not findPath(root, path1, nr1) or not findPath(root, path2, nr2)): 
        return -1 
    
    