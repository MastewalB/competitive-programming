class AugmentedBST:

    def __init__(self, value, left=None, right=None):
        self.index = 1
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

    def insert(self, value, node=None, root=True, augment=1):
        if root:
            node = self
        if node is None:
            self.index += augment
            return AugmentedBST(value)

        if value < node.value:
            node.left = self.insert(value, node.left, True, augment=1)
            

        elif value > node.value:
            node.right = self.insert(value, node.right, True,augment=1)

        else:
            return node

        return node

    def inorder_traversal(self):
        self.node_list = []
        self._inorder_traversal(self)
        print(self.node_list)

    def _inorder_traversal(self, node):
        if node != None:
            self._inorder_traversal(node.left)
            self.node_list.append([node.index, node.value])
            self._inorder_traversal(node.right)


value = input("Enter the first value (root) of your Binary Search Tree:")
tree = AugmentedBST(value)

while True:
    tree.insert(value)
    print("Your Binary Search Tree so far:")
    print("")
    print("In-order traversal:")
    tree.inorder_traversal()
    print("")
    value = input("Enter a new value or exit to quit...:")
    if value == "exit":
        break
