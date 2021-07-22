from BinarySearchTree_Node import BinarySearchTree



def check(node):
    if node == None:
        return 0
    

    left = check(node.left)
    if left == -1:
        return -1
    
    right = check(node.right)
    if right == -1:
        return -1

    difference = left - right

    if abs(difference) > 1:
        return -1

    return 1 + max(left, right)


    
    
    



def check_balance(tree):
    result = check(tree.root)
    if result > 0:
        return True
    else:
        return False

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

print(check_balance(tree))