# Right view of a binary tree LC 199

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
    
    def rightSideView(self, root):
        if not root:
            return []
        q = []
        q.append(root)
        res = []
        while q:
            res.append(q[-1].val)  # Append the last element of the queue (rightmost node)
            for _ in range(len(q)):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
    

arr=[1,2,3,"N",5,"N",4]
tree=TreeNode() # type: ignore
root=tree.buildTree(arr)
print(tree.rightSideView(root)) 