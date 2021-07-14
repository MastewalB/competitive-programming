import os


class BinarySearchTree:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def find(self, value):
        node = self
        while node:
            if value < node.val:
                node = node.left

            elif value > node.val:
                node = node.right

            else:
                return node

    def get_max(self):
        node = self
        while node and node.right:
            node = node.right
        return node

    def get_min(self):
        node = self
        while node and node.left:
            node = node.left
        return node

    def insert(self, value, node=None, root=True):
        if root:
            node = self
        if node is None:
            return BinarySearchTree(value)

        if value < node.value:
            node.left = self.insert(value, node.left, False)

        elif value > node.value:
            node.right = self.insert(value, node.right, False)

        else:
            return node

        return node

    def delete(self, value, node=None, root=True):
        if root:
            node = self
        if node is None:
            return None

        if value < node.value:
            node.left = self.delete(value, node.left, False)
        elif value > node.value:
            node.right = self.delete(value, node.right, False)

        elif node.left and node.right:
            successor = self.get_min(node.right)
            node.val = successor.val
            node.right = self.delete(node.val, node.right, False)

        else:
            if node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left

    def preorder_traversal(self):
        self.node_list = []
        if node != None:
            self.node_list.append(node.value)
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

        print(self.node_list)

    def inorder_traversal(self):
        self.node_list = []
        if node != None:
            self.inorder_traversal(node.left)
            self.node_list.append(node.value)
            self.inorder_traversal(node.right)

        print(self.node_list)

    def postorder_traversal(self):
        self.node_list = []
        if node != None:
            self.postorder_traversal(node.right)
            self.postorder_traversal(node.left)
            self.node_list.append(node.value)

        print(self.node_list)
