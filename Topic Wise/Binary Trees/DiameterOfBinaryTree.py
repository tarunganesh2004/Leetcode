# Diameter of Binary Tree LC 543

# Given a binary tree, the diameter (also known as the width) is defined as the number of edges on the longest path between two leaf nodes in the tree. 
# This path may or may not pass through the root.task is to find the diameter of the tree.

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
    
    # approach to find diameter is to find the diameter of left subtree and right subtree , and path through the root(left height+right height)
    # and then take the maximum of the three
    # This approach leads to O(n^2) time complexity & TLE for large inputs
    def height(self,root):
        if not root:
            return 0
        return 1+max(self.height(root.left),self.height(root.right))
    
    def diameter(self,root):
        if not root:
            return 0
        left_height=self.height(root.left)
        right_height=self.height(root.right)

        # diameter of left subtree
        left_diameter=self.diameter(root.left)
        # diameter of right subtree
        right_diameter=self.diameter(root.right)

        # diameter passing through the root
        diameter_through_root=left_height+right_height
        return max(left_diameter,right_diameter,diameter_through_root)
    
    # optimized approach to find diameter is to find the height of the tree and diameter of the tree in a single traversal
    # O(n) TC 
    def height_and_diameter(self,root):
        if root is None:
            return (0,0) # (height,diameter)
        
        left_height,left_diameter=self.height_and_diameter(root.left)
        right_height,right_diameter=self.height_and_diameter(root.right)

        # cur_node height
        cur_height=1+max(left_height,right_height)

        # diameter through the root
        diameter_through_root=left_height+right_height

        # max of all diameters
        cur_diameter=max(left_diameter,right_diameter,diameter_through_root)
        return (cur_height,cur_diameter)
    
    def diameter_optimized(self,root):
        return self.height_and_diameter(root)[1]
    

arr=[1,2,3]
tree=TreeNode(None)
root=tree.build_tree(arr)
print(tree.diameter(root)) # type: ignore # 2

arr=[1,2,3,4,5]
tree=TreeNode(None)
root=tree.build_tree(arr)
print(tree.height_and_diameter(root)) # type: ignore # 3