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
        self._preorder_traversal(self)
        print(self.node_list)

    def _preorder_traversal(self, node):
        if node != None:
            self.node_list.append(node.value)
            self._preorder_traversal(node.left)
            self._preorder_traversal(node.right)

    def inorder_traversal(self):
        self.node_list = []
        self._inorder_traversal(self)
        print(self.node_list)

    def _inorder_traversal(self, node):
        if node != None:
            self._inorder_traversal(node.left)
            self.node_list.append(node.value)
            self._inorder_traversal(node.right)

    def postorder_traversal(self):
        self.node_list = []
        self._postorder_traversal(self)
        print(self.node_list)

    def _postorder_traversal(self, node):
        if node != None:
            self._postorder_traversal(node.left)
            self._postorder_traversal(node.right)
            self.node_list.append(node.value)


value = input("Enter the first value (root) of your Binary Search Tree:")
tree = BinarySearchTree(value)

while True:
    tree.insert(value)
    print("Your Binary Search Tree so far:")
    print("")
    print("In-order traversal:")
    tree.inorder_traversal()
    print("")
    print("Pre-order traversal:")
    tree.preorder_traversal()
    print("")
    print("Post-order traversal:")
    tree.postorder_traversal()
    print("")
    value = input("Enter a new value or exit to quit...:")
    if value == "exit":
        break
