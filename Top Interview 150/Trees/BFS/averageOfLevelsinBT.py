# Average of Levels in Binary Tree LC 637

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
    
    def averageOfLevels(self, root):
        if not root:
            return []
        q = []
        q.append(root)
        res = []
        while q:
            n = len(q)
            sum = 0
            for _ in range(n):
                node = q.pop(0)
                sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(sum/n)
        return res
    
arr=[3,9,20,"N","N",15,7]
tree=TreeNode() 
root=tree.buildTree(arr)
print(tree.averageOfLevels(root))  # Output: [3.0, 14.5, 11.0]