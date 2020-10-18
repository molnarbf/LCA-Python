# Python implementation for finding the Lowest Common Ancestor in a Binary Tree
class Node:
    def __init__(self, key = None):
        self.key = key
        self.left = None
        self.right = None

# find path from root node to given root
def findPath(root, path, k):
    if root is None:
        return False
    
    path.append(root.key)
    if root.key == k:
        return True

    if ((root.left is not None and findPath(root.left, path, k)) or (root.right is not None and findPath(root.right, path, k))):
        return True

    path.pop()
    return False

# find paths from root node to given nodes (LCA)
def findLCA(root, nr1, nr2):
    path1 = []
    path2 = []

    # find path1 and path2 from root and return -1 if either node is not present
    if not findPath(root, path1, nr1) or not findPath(root, path2, nr2): 
        return -1 
    
    i = 0
    while i < len(path1) and i < len(path2):
        if path2[i] != path1[i]:
            break
        i += 1
    return path1[i-1]
    