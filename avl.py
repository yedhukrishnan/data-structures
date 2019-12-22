"""
AVL Tree Operations
===================


"""

class Node:
    def __init__(self, left=None, right=None, value=None):
        self.left = left
        self.right = right
        self.value = value

class AVL:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_value(value, self.root)

    """ Private Functions """

    def _insert_value(self, value, node):
        if node == None:
            return Node(value = value)

        if node.value <= value:
            node.right = self._insert_value(value, node.right)
        else:
            node.left  = self._insert_value(value, node.left)

        return node

