class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)

            self.result = max(self.result, left + right + 2)
            return 1 + max(left, right)

        dfs(root)
        return self.result


Solution()
