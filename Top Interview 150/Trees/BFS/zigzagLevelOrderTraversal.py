# ZigZag Level Order Traversal LC 103

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
    
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        q = []
        q.append(root)
        res = []
        flag = 0
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
            if flag%2==1:
                level = level[::-1] # Reverse the level list
            res.append(level)
            flag+=1
        return res
    
arr=[3,9,20,"N","N",15,7]
tree=TreeNode()
root=tree.buildTree(arr)
print(tree.zigzagLevelOrder(root))  # Output: [[3], [20, 9], [15, 7]]