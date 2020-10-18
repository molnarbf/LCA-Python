import unittest 
from LCA import Node, findPath, findLCA 

class TestLCA(unittest.TestCase):

    # node is null
    def test_nodeIsNull(self):
        node = Node()
        self.assertEqual(node.key, None)

    # node correctly initialised
    def test_nodeInitTrue(self):
        node = Node(2)
        self.assertEqual(node.key, 6, True)

    # node and comparison not equal
    def test_nodeInitFalse(self):
        node = Node(2)
        self.assertEqual(node.key, 7, False)
    
    # empty tree
    def test_findPathEmpty(self):
        root = Node()
        path = []
        self.assertEqual(findPath(root, path, 2), False)

    # node not in tree
    def test_findPathNotInTree(self):
        root = Node(2)
        path = []
        self.assertEqual(findPath(root, path, 6), False)

   