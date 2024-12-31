# LC 2471 Minimum Number of Operations to sort a Binary Tree by level

from collections import deque

from cv2 import sort

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.right=right
        self.left=left

class Solution:
    def buildTree(self,arr):
        n=len(arr)
        root=TreeNode(arr[0])
        if n==0 or arr[0]==None:
            return None
        q=deque()
        q.append(root)
        i=1
        while i<n:
            cur=q.popleft()
            if arr[i]!=None:
                cur.left=TreeNode(arr[i])
                q.append(cur.left)
            i+=1
            if i>n:
                break
            if i<n and arr[i]!=None:
                cur.right=TreeNode(arr[i])
                q.append(cur.right)
            i+=1
        return root

    def minSwaps(self,arr):
        # temp=arr.copy()
        # temp.sort()
        sorted_nums=sorted(arr)
        idx_map={num:i for i,num in enumerate(sorted_nums)}

        ans=0
        for i in range(len(arr)):
            if arr[i]!=sorted_nums[i]:
                ans+=1

                j=idx_map[sorted_nums[i]]
                arr[i],arr[j]=arr[j],arr[i]
                # idx_map[arr[i]]=i
                idx_map[arr[j]]=j
                
                # crct_idx=arr.index(temp[i])
                # arr[i],arr[crct_idx]=arr[crct_idx],arr[i]
            
        return ans
    
    def minOperations(self,root):
        q=deque()
        q.append(root)
        level=0
        ans=0
        while q:
            n=len(q)
            l=[]
            for i in range(n):
                cur=q.popleft()
                l.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            
            ans+=self.minSwaps(l)
            level+=1

        return ans
    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.val,end=" ")
            self.inorder(root.right)
    
    def preorder(self,root):
        if root:
            print(root.val,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

arr = [1, 4, 3, 7, 6, 8, 5, None, None, None, None, 9, None, 10]
sol=Solution()
root=sol.buildTree(arr)
sol.preorder(root)
print()

print(sol.minOperations(root))