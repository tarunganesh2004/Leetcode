# LC 515 Find largest value in each row
from collections import deque


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.right=right
        self.left=left

class Solution:
    def largestValues(self,root):
        if not root:
            return []
        q=deque([root])
        ans=[]
        while q:
            n=len(q)
            max_val=float('-inf')
            for i in range(n):
                cur=q.popleft()
                max_val=max(max_val,cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            ans.append(max_val)
        return ans
    
    