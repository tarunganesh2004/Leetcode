# Level Order Traversal LC 102

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
    
    def levelOrder(self, root):
        if not root:
            return []
        q = []
        q.append(root)
        res = []
        while q:
            n = len(q)
            level = []
            for _ in range(n):
                node = q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res
    
arr=[3,9,20,"N","N",15,7]
tree=TreeNode()
root=tree.buildTree(arr)
print(tree.levelOrder(root))  # Output: [[3], [9, 20], [15, 7]]