# Lowest Common Ancestor of Deeperst Leaves LC 1123

arr=[3,5,1,6,2,0,8,None,None,7,4]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def buildTree(arr):
        if not arr:
            return None
        root=TreeNode(arr[0])
        queue=[root]
        i=1
        while queue and i<len(arr):
            node=queue.pop(0)
            if arr[i] is not None:
                node.left=TreeNode(arr[i])
                queue.append(node.left)
            i+=1
            if i>len(arr):
                break
            if i<len(arr) and arr[i] is not None:
                node.right=TreeNode(arr[i])
                queue.append(node.right)
            i+=1
        return root
    
class Solution:
    def lcaDeepestLeaves(self,root):
        self.lca,self.deepest=None,0
        def dfs(node,depth):
            self.deepest=max(self.deepest,depth)
            if not node:
                return depth
            left=dfs(node.left,depth+1)
            right=dfs(node.right,depth+1)
            if left==right==self.deepest:
                self.lca=node
            return max(left,right)
        dfs(root,0)
        return self.lca
    

root=TreeNode.buildTree(arr)
sol=Solution()
lca_node=sol.lcaDeepestLeaves(root)
print(lca_node.val if lca_node else None)