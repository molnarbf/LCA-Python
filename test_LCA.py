import unittest 
from LCA import Node 

class TestLCA(unittest.TestCase):

    def test_nodeIsNull(self):
        node = Node()
        self.assertEqual(node.key, None)

    def test_nodeInitTrue(self):
        node = Node(2)
        self.assertEqual(node.key, 6, True)

    def test_nodeInitFalse(self):
        node = Node(2)
        self.assertEqual(node.key, 7, False)
    
    