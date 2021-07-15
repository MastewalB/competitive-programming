class Node:
    def __init__(self, value):
        self.index = 0
        self.value - value
        self.parent = None
        self.left = None
        self.right = None

    def get_parent(self):
        return self.parent

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right


class BinarySearchTree:
    def __init__(self, root):
        self.root = Node(root)
