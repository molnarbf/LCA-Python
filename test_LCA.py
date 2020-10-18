import unittest 
from LCA import Node 

class TestLCA(unittest.TestCase):

    def test_nodeIsNull(self):
        node = Node()
        self.assertEqual(node.key, None)

