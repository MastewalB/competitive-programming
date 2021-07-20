from BinarySearchTree_Node import BinarySearchTree


levels = []
def level_traversal(bst, node = None):
    queue = []

    if node == None:
        node = bst.root

    queue.push([node])
    while len(stack) > 0:
        queue.append([])
        for i in range(len(queue[0])):
            for child in queue[0][i].children:
                if child != None:
                    queue[1].append(child)
        
        #remove/pop the parent 


    



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
