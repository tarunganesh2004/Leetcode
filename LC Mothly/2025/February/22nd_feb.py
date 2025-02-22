# Recover a Tree from preorder traversal LC 1028

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def print_tree(self, level=0, prefix="Root: "):
        print(" " * (level * 4) + prefix + str(self.val))
        if self.left:
            self.left.print_tree(level + 1, "L--- ")
        if self.right:
            self.right.print_tree(level + 1, "R--- ")

class Solution:
    def recoverFromPreorder(self,S):
        def dfs(S,depth):
            if not S:
                return None
            i=0
            while i<len(S) and S[i]=='-':
                i+=1
            if i!=depth:
                return None
            j=i
            while j<len(S) and S[j]!='-':
                j+=1
            node=TreeNode(int(S[i:j]))
            node.left=dfs(S[j:],depth+1)
            node.right=dfs(S[j:],depth+1)
            return node
        return dfs(S,0)
    
obj=Solution()
traversal="1-2--3--4-5--6--7"
root=obj.recoverFromPreorder(traversal)
root.print_tree() # type: ignore