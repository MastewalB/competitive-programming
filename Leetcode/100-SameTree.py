class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p, q):
    if p == None and q == None:
        return True
    if p == None or q == None:
        return False

    if p.val == q.val:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
    else:
        return False


p = TreeNode(0, 1, 2)
q = TreeNode(0, 1, 2)

print(is_same_tree(p, q))
