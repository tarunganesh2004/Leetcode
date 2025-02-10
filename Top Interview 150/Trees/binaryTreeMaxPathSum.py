# Binary Tree Maximum Path Sum LC 124(Hard)

# Given a non-empty binary tree, find the maximum path sum.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def buildTree(self,arr):
        if not arr or arr[0]=="N":
            return None
        root = TreeNode(arr[0])
        q=[]
        q.append(root)
        i=1
        while i<len(arr) and q:
            node = q.pop(0)
            if arr[i]!="N":
                node.left = TreeNode(arr[i])
                q.append(node.left)
            i+=1
            if i>=len(arr):
                break
            if i<len(arr) and arr[i]!="N":
                node.right = TreeNode(arr[i])
                q.append(node.right)
            i+=1

        return root

class Solution:
    def maxPathSum(self,root): # O(n) time and O(h) space
        if not root:
            return 0
        
        self.maxSum=float("-inf")
        def dfs(cur_node):
            if not cur_node:
                return 0
            left=dfs(cur_node.left)
            right=dfs(cur_node.right)
            left=0 if left<0 else left  # if left is negative, we don't need it
            right=0 if right<0 else right 
            total=left+right+cur_node.val

            if total>self.maxSum:
                self.maxSum=total
            return max(left,right)+cur_node.val
        
        dfs(root)
        return self.maxSum
    
arr=[-10,9,20,"N","N",15,7]
root=TreeNode().buildTree(arr)
print(Solution().maxPathSum(root)) # 42