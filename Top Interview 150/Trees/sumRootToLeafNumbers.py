# Sum Root to Leaf Numbers LC 129(Medium)

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
    def sumNumbers(self,root):
        if not root:
            return 0
        self.res=0
        def dfs(cur_node,cur_sum):
            if not cur_node:
                return
            cur_sum=cur_sum*10+cur_node.val
            if not cur_node.left and not cur_node.right:
                self.res+=cur_sum
            dfs(cur_node.left,cur_sum)
            dfs(cur_node.right,cur_sum)
        dfs(root,0)
        return self.res
    
arr=[1,2,3]
root=TreeNode().buildTree(arr)
print(Solution().sumNumbers(root)) # 25