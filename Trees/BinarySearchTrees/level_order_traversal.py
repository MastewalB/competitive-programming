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
        #print(front[0].value)
        for i in range(len(front)):
            for child in front[i].children:
                
                if child != None:
                    new.append(child)
                    print(new)
        print(queue.size())
        levels.append(queue.dequeue())
        #print(levels)
        
    queue.enqueue(new)
        
    
    #print(levels)


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
#tree.print()

level_traversal(tree)
