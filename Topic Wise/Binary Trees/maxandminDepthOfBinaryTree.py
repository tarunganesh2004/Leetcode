# Maximum and Minimum Depth of Binary tree 

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def build_tree(self, arr):
        if not arr or arr[0] == "N":
            return None
        root = TreeNode(arr[0])
        i = 1
        q = []
        q.append(root)
        while q:
            node = q.pop(0)
            if i < len(arr) and arr[i] != "N":
                node.left = TreeNode(arr[i])
                q.append(node.left)
            i += 1
            if i >= len(arr):
                break
            if i < len(arr) and arr[i] != "N":
                node.right = TreeNode(arr[i])
                q.append(node.right)
            i += 1
        return root

    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def minDepth(self, root):
        if not root:
            return 0
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)


# Test code
root_arr = [3, 9, 20, "N", "N", 15, 7]
tree = TreeNode(None)  
root = tree.build_tree(root_arr) 

print(tree.maxDepth(root))  
print(tree.minDepth(root))  