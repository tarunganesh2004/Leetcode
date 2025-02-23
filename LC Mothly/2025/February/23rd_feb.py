# Construct Binary Tree From Preorder and postorder traversal LC 889

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

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.val)
        if self.right:
            self.right.inorder()

class Solution:
    def constructFromPrePost(self,pre,post):
        if not pre:
            return None
        root=TreeNode(pre[0])
        if len(pre)==1:
            return root
        L=post.index(pre[1])+1
        root.left=self.constructFromPrePost(pre[1:L+1],post[:L])
        root.right=self.constructFromPrePost(pre[L+1:],post[L:-1])
        return root
    
obj=Solution()
pre=[1,2,4,5,3,6,7]
post=[4,5,2,6,7,3,1]
root=obj.constructFromPrePost(pre,post)
root.print_tree() # type: ignore