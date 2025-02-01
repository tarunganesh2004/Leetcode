# Kth Smallest Element in a BST

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def buildTree(arr):
        if not arr or arr[0] is None:
            return None
        root = TreeNode(arr[0])
        for i in range(1,len(arr)):
            if arr[i] is not None:
                TreeNode.insert(root,arr[i])
        return root
    
    @staticmethod
    def insert(root,val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = TreeNode.insert(root.left,val)
        else:
            root.right = TreeNode.insert(root.right,val)
        return root
    
    @staticmethod
    def inorder(root):
        if not root:
            return []
        return TreeNode.inorder(root.left) + [root.val] + TreeNode.inorder(root.right)

class Solution:
    def kthSmallest(self,root,k):
        l=TreeNode.inorder(root)  # noqa: E741
        return l[k-1]
    


arr=[3,1,4,None,2]
k=1
root = TreeNode.buildTree(arr)
sol = Solution()
print(sol.kthSmallest(root,k))