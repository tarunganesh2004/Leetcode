# Binary Tree Right Side View LC 199

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
    def rightSideView(self,root):
        if not root:
            return []
        
        q=deque([root])
        rightView=[]
        while q:
            rightView.append(q[-1].val)
            for _ in range(len(q)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return rightView
    
arr=[1,2,3,None,5,None,4]
root=TreeNode().buildTree(arr)
sol=Solution()
print(sol.rightSideView(root)) #[1,3,4]