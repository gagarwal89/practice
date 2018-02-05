from tree import Tree
from tree_node import TreeNode

class BinarySearchTree(Tree):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
            return

        self.insert_internal(data, self.root)

    def search(self, data):
        if self.root is None:
            return
        
        return self.search_internal(data, self.root)

    """ Internal methods """
    def insert_internal(self, data, current):
        if current is None:
            return

        if data < current.data:
            if current.left is None:
                current.left = TreeNode(data)
            else:
                self.insert_internal(data, current.left)
        else:
            if current.right is None:
                current.right = TreeNode(data)
            else:
                self.insert_internal(data, current.right)

    def search_internal(self, data, current):
        if current is None:
            return False

        if data < current.data:
            return self.search_internal(data, current.left)
        elif data == current.data:
            return True
        else:
            return self.search_internal(data, current.right)
