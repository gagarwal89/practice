from tree_node import TreeNode

class Tree(object):
    def __init__(self):
        self.root = None

    def inorder(self):
        self.inorder_internal(self.root)

    def preorder(self):
        self.preorder_internal(self.root)

    def postorder(self):
        self.postorder_internal(self.root)

    def height(self):
        return self.height_internal(self.root)

    def inorder_internal(self, current):
        if current is None:
            return

        self.inorder_internal(current.left)
        print str(current.data) + "->"
        self.inorder_internal(current.right)

    def preorder_internal(self, current):
        if current is None:
            return

        print current.data
        self.preorder_internal(current.left)
        self.preorder_internal(current.right)

    def postorder_internal(self, current):
        if current is None:
            return

        self.postorder_internal(current.left)
        self.postorder_internal(current.right)
        print current.data

    def height_internal(self, current):
        if current is None:
            return 0

        left_height = self.height_internal(current.left)
        right_height = self.height_internal(current.right)

        return 1 + max(left_height, right_height)