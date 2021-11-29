from BinarySearchTree_Node import Node, BinarySearchTree


def construct(array):
    length = len(array)
    if length == 1:
        return Node(array[0])
    elif length == 0:
        return

    root = Node(array[length//2])
    root.left = construct(array[0:length//2])
    root.right = construct(array[length//2+1:])

    return root


def construct_bst(array):
    tree = BinarySearchTree(array[len(array)//2])
    tree.root.left = construct(array[0:len(array)//2])
    tree.root.right = construct(array[len(array)//2+1:])

    return tree


array = [0, 1, 2, 9, 3, 6, 7, 8, 12, 20]
tree = construct_bst(array)
tree.print(0)
print(tree.root.value)
