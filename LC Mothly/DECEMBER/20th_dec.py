# LC 2415
# Reverse Odd levels of Binary Tree

from collections import deque


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.right=right
        self.left=left

class Solution:
    def reverseOddLevels(self,root):
        q=deque()
        q.append(root)
        level=0
        while q:
            n=len(q)
            l=[]
            for i in range(n):
                node=q.popleft()
                l.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if level%2==1:
                left=0
                right=len(l)-1
                while left<right:
                    l[left].val,l[right].val=l[right].val,l[left].val
                    left+=1
                    right-=1
            
            level+=1

        return root
    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.val,end=" ")
            self.inorder(root.right)
        
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right.left=TreeNode(6)
root.right.right=TreeNode(7)

sol=Solution()
sol.inorder(root)
print()
root=sol.reverseOddLevels(root)
sol.inorder(root)
print()