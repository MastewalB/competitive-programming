class Node:
    def __init__(self, value):
        self.index = 0
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.children = [self.get_left(), self.get_right()]

    def get_parent(self):
        return self.parent

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right


class BinarySearchTree:
    def __init__(self, root):
        self.root = Node(root)

    def find(self, value):
        node = self.root
        while node:
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                return node

    def is_leaf(self, element):
        node = self.find(element)
        if node:
            if node.left or node.right:
                return False
            return True

    def get_max(self, node=None):
        if node is None:
            node = self.root
        while node and node.right:
            node = node.right

        return node

    def get_min(self, node=None):
        if node is None:
            node = self.root
        while node and node.left:
            node = node.left

        return node

    def successor(self, element):
        node = self.find(element)
        if node.right:
            successor = self.get_min(node.right)
            return successor
        return None

    def predecessor(self, element):
        node = self.find(element)
        if node.left:
            predecessor = self.get_max(node.left)
            return predecessor

        return None

    def insert(self, element):
        node = self.root
        parent_node = None
        new_element = Node(element)

        while True:
            if element > node.value:
                parent_node = node
                node = node.right
                if node == None:
                    parent_node.right = new_element
                    parent_node.children[1] = new_element
                    return

            elif element < node.value:
                parent_node = node
                node = node.left
                if node == None:
                    parent_node.left = new_element
                    parent_node.children[0] = new_element
                    return

            else:
                print("No duplicate elements allowed")
                return

    def delete(self, element):
        parent = self.root
        node = self.root
        is_left = False

        while node.value != element:
            parent = node
            if element < node.value:
                node = node.left
                is_left = True
            else:
                is_left = False
                node = node.right
            if node == None:
                print("No such element")
                return

        if self.is_leaf(node.value):
            if is_left:
                parent.left = None
            else:
                parent.right = None

        else:
            if node.right == None:
                if node == self.root:
                    self.root = node.left
                elif is_left:
                    parent.left = node.left
                else:
                    parent.right = node.left

            elif node.left == None:
                if node == self.root:
                    self.root = node.right
                elif is_left:
                    parent.left = node.right
                else:
                    parent.right = node.right

            else:
                successor = self.successor(node.value)
                if node == self.root:
                    self.root = successor
                elif is_left:
                    self.delete(successor.value)
                    parent.left = successor
                else:
                    self.delete(successor.value)
                    parent.right = successor

                successor.left = node.left
                successor.right = node.right

    def inorder_traversal(self, node=None):
        if node == None:
            node = self.root
        self.node_list = []
        self._inorder_traversal(node)
        return self.node_list

    def _inorder_traversal(self, node):
        if node != None:
            self._inorder_traversal(node.left)
            self.node_list.append(node)
            self._inorder_traversal(node.right)

    def preorder_traversal(self, node=None):
        if node == None:
            node = self.root
        self.node_list = []
        self._preorder_traversal(node)
        return self.node_list

    def _preorder_traversal(self, node):
        if node != None:
            self.node_list.append(node)
            self._preorder_traversal(node.left)
            self._preorder_traversal(node.right)

    def postorder_traversal(self, node=None):
        if node == None:
            node = self.root
        self.node_list = []
        self._postorder_traversal(node)
        return self.node_list

    def _postorder_traversal(self, node):
        if node != None:
            self._postorder_traversal(node.left)
            self._postorder_traversal(node.right)
            self.node_list.append(node)

    def print(self, traversal = 0):
        
        node_list = []
        if traversal == 0:
            node_list = self.inorder_traversal()
        elif traversal == 1:
            node_list = self.preorder_traversal()
        elif traversal == 2:
            node_list = self.postorder_traversal()

        for i in range(len(node_list)):
            print(node_list[i].value, end=" ")
        print()

    def in_range(self, root, start_node, end_node):
        """Function verifies that all nodes beneath root are in between start_node and end_node"""

        node_list = self.inorder_traversal(root)
        node_list.pop()
        deviates = {}
        for i in range(len(node_list)):
            if node_list[i].value > end_node.value:
                deviates[end_node.value] = node_list[i].value
            elif node_list[i].value < start_node.value:
                deviates[start_node.value] = node_list[i].value
        return deviates

    def validate_bst(self, node=None):
        if node == None:
            node = self.root

        if node == self.root:

            if node.left:
                if node.left.value > node.value:
                    print("BST Violated at " + str(node.value))
                self.validate_bst(node.left)

            if node.right:
                if node.right.value < node.value:
                    print("BST Violated at " + str(node.value))
                self.validate_bst(node.right)

        else:

            if node.left:
                deviates = self.in_range(node.left, node.left, node)
                print(deviates)
                self.validate_bst(node.left)

            elif node.right:
                deviates = self.in_range(node.right, node, node.right)
                print(deviates)
                self.validate_bst(node.right)


# tree = BinarySearchTree(40)
# tree.insert(20)
# tree.insert(10)
# tree.insert(5)
# tree.insert(30)
# tree.insert(50)
# tree.insert(60)
# tree.insert(67)
# tree.insert(78)
# tree.insert(7)
# tree.insert(45)
# tree.insert(35)
# tree.insert(55)
# tree.insert(62)

# tree = BinarySearchTree(7)
# tree.insert(6)
# tree.insert(9)
# tree.insert(0)
# tree.insert(2)
# tree.insert(8)
# tree.insert(12)
# tree.insert(1)
# tree.insert(3)
# tree.insert(10)
# tree.insert(11)
# node = tree.find(2)
# node.left = Node(4)
# tree.print()

# tree.validate_bst()
