# # Find Elements in Contaminated Binary Tree LC 1261

# Given a binary tree with the following rules:

# root.val == 0
# For any treeNode:
# If treeNode.val has a value x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
# If treeNode.val has a value x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
# Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

# Implement the FindElements class:

# FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
# bool find(int target) Returns true if the target value exists in the recovered binary tree.

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class FindElements:
    def __init__(self,root):
        self.root=root
        self.root.val=0
        self.visited=set()

        def recover(node):
            if node:
                self.visited.add(node.val)
                if node.left:
                    node.left.val=2*node.val+1
                    recover(node.left)
                if node.right:
                    node.right.val=2*node.val+2
                    recover(node.right)
        recover(self.root)

    def find(self,target):
        return target in self.visited
    
arr=[-1,-1,-1,-1,-1]
root=TreeNode(0)
root.left=TreeNode(1)
root.right=TreeNode(2)
root.left.left=TreeNode(3)
root.left.right=TreeNode(4)
root.right.left=TreeNode(5)
root.right.right=TreeNode(6)

obj=FindElements(root)
print(obj.find(1))
print(obj.find(3))
print(obj.find(5))
print(obj.find(7))


# Another approach is to use dfs
class findElements:
    def __init__(self,root):
        def dfs(node,val):
            if not node:
                return
            self.visited.add(val)
            dfs(node.left,2*val+1)
            dfs(node.right,2*val+2)
        self.visited=set()
        dfs(root,0)

    def find(self,target):
        return target in self.visited