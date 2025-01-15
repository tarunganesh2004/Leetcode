# Maximum Level Sum of a Binary Tree LC 1161
from collections import deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

    def buildTree(self,arr):
        if not arr:
            return None
        root=TreeNode(arr[0])
        q=deque([root])
        i=1
        while i<len(arr):
            node=q.popleft()
            if arr[i] is not None:
                node.left=TreeNode(arr[i])
                q.append(node.left)
            i+=1
            if i>=len(arr):
                break
            if i<len(arr) and arr[i] is not None:
                node.right=TreeNode(arr[i])
                q.append(node.right)
            i+=1
        return root


class Solution:
    def maxLevelSum(self,root):
        if not root:
            return 0
        q=deque([root])
        level=1
        maxSum=float('-inf')
        maxLevel=1
        while q:
            levelSum=0
            for _ in range(len(q)):
                node=q.popleft()
                levelSum+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if levelSum>maxSum:
                maxSum=levelSum
                maxLevel=level
            level+=1
        return maxLevel
    
arr=[1,7,0,7,-8,None,None]
root=TreeNode().buildTree(arr)
sol=Solution()
print(sol.maxLevelSum(root)) #2