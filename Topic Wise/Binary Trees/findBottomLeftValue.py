# Find Bottom Left Value LC 513

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def build_tree(self,arr):
        if not arr or arr[0] == 'N':
            return None
        
        root = TreeNode(arr[0])
        i = 1
        q = []
        q.append(root)
        while i < len(arr) and q:
            node = q.pop(0)
            if arr[i] != 'N':
                node.left = TreeNode(arr[i])
                q.append(node.left)
            i += 1
            if i>=len(arr):
                break
            if i < len(arr) and arr[i] != 'N':
                node.right = TreeNode(arr[i])
                q.append(node.right)
            i += 1

        return root
    
    def find_bottom_left_value(self,root):
        if not root:
            return None
        q = []
        q.append(root)
        while q:
            node = q.pop(0)
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        return node.data
    
arr=[2,1,3]
root=TreeNode(arr[0])
root=root.build_tree(arr)
print(root.find_bottom_left_value(root)) # type: ignore