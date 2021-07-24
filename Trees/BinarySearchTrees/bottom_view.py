from BinarySearchTree_Node import BinarySearchTree

visibles = []
def bottom_view(node, index):
    if node is None:
        return
    
    print(index, "node -", node.value)
    if node.left:
        index += 1
        bottom_view(node.left, index)
    
        if index >= 0:
            index -= 1
        elif index < 0:                
            index += 1

        
    
    if node.right:
        index -= 1
        bottom_view(node.right, index)
        if index >= 0:
            index -= 1
        elif index < 0:                
            index += 1
        

    
    
            


tree = BinarySearchTree(8)
tree.insert(6)
tree.insert(10)
tree.insert(4)
tree.insert(7)
tree.insert(9)
tree.insert(12)
tree.insert(13)
tree.insert(2)
tree.insert(5)
tree.insert(1)
tree.insert(3)

bottom_view(tree.root, 0)
