from BinarySearchTree_Node import BinarySearchTree
from Queue import Queue


def level_traversal(bst, node=None):
    queue = Queue()
    levels = []

    if node == None:
        node = bst.root

    queue.enqueue([node])
    while queue.size() > 0:
        new = []

        front = queue.peek()

        for i in range(len(front)):
            for child in front[i].children:

                if child != None:
                    new.append(child)

        levels.append(queue.dequeue())

        if new != []:
            queue.enqueue(new)

    return levels


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
# tree.print()

levels = level_traversal(tree)
for i in range(len(levels)):
    for j in range(len(levels[i])):
        print(levels[i][j].value, end=" ")
    print()
