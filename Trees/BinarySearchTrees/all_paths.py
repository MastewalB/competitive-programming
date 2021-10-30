from BinarySearchTree_Node import BinarySearchTree

paths = []


def paths_under_node(node, path=[]):
    if node is None:
        return
    path.append(node.value)

    if node.left == None and node.right == None:
        paths.append(list(path))
        path.pop()

    else:
        paths_under_node(node.left, path)
        paths_under_node(node.right, path)
        path.pop()


tree = BinarySearchTree(7)
tree.insert(6)
tree.insert(9)
tree.insert(0)
tree.insert(2)
tree.insert(8)
tree.insert(12)
tree.insert(1)
tree.insert(3)
tree.insert(10)
tree.insert(11)

paths_under_node(tree.root)
print("All Paths - ", paths)
