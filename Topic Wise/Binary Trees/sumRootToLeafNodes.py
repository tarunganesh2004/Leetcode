# Sum Root to leaf numbers LC 129

class TreeNode:
    def __init__(self,val):
        self.val = val
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
    
    def sum_root_to_leaf(self,root):
        if not root:
            return 0
        self.res=0
        self.dfs(root,0)
        return self.res
    
    def dfs(self,root,curr_sum):
        if not root:
            return
        curr_sum=curr_sum*10+root.val
        if not root.left and not root.right:
            self.res+=curr_sum
            return
        self.dfs(root.left,curr_sum)
        self.dfs(root.right,curr_sum)

arr=[1,2,3]
root=TreeNode(arr[0])
root=root.build_tree(arr)
print(root.sum_root_to_leaf(root)) # type: ignore