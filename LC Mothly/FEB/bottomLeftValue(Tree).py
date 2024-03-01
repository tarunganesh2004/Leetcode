# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if root.left is None and root.right is None:
                return (root.val, depth)
            l = None
            if root.left is not None:
                l = dfs(root.left, depth + 1)
            r = None
            if root.right is not None:
                r = dfs(root.right, depth + 1)

            if r is None:
                return l
            if l is None:
                return r

            if r[1] > l[1]:
                return r
            return l

        return dfs(root, 0)[0]
