# 2458 Height of Binary Tree after subtree Removal Queries

from typing import List,Optional
from functools import lru_cache
from collections import defaultdict

class TreeNode:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

def insert_level_order(arr:List[Optional[int]],root:Optional[TreeNode],i:int,n:int)->Optional[TreeNode]:
    if i<n and arr[i] is not None:
        temp=TreeNode(arr[i])
        root=temp

        root.left=insert_level_order(arr,root.left,2*i+1,n) # type: ignore
        root.right=insert_level_order(arr,root.right,2*i+2,n) # type: ignore

    return root


class Solution:
    def treeQueries(self,root:Optional[TreeNode],queries:List[int]) -> List[int]:
        @lru_cache(None)
        def height(node):
            if not node:
                return 0
            
            return 1+max(height(node.left),height(node.right))
        
        dict1=defaultdict(int)

        def dfs(node,depth,max_val):
            if not node:
                return
            
            dict1[node.val]=max_val

            dfs(node.left,depth+1,max(max_val,depth+1,height(node.right)))
            dfs(node.right,depth+1,max(max_val,depth+1,height(node.left)))

        dfs(root,0,0)

        return [dict1[query] for query in queries]
    

# class SolutionBruteForce:
#     def treeQueries(self,root,queries): # Approach is to remove the subtree corresponding to the query and then calculate the height of the tree

#         if not root:
#             return []
        
#         def remove_subtree(node,query):
#             if not node:
#                 return node
            
#             if node.val==query:
#                 return None # Removing the subtree
            
#             node.left=remove_subtree(node.left,query)
#             node.right=remove_subtree(node.right,query)

#             return node
        
#         def height(node):
#             if not node:
#                 return 0
            
#             return 1+max(height(node.left),height(node.right))
        
#         res=[]

#         for query in queries:
#             import copy
#             new_root=copy.deepcopy(root)
#             new_root=remove_subtree(new_root,query)
#             res.append(height(new_root))

#         return res
        

def main():
    input_str = input()

    input_list = [int(x) if x != "null" else None for x in input_str.split(",")]

    root = insert_level_order(input_list, None, 0, len(input_list))

    queries = list(map(int, input().split(",")))

    solution = Solution()
    # solution_brute_force = SolutionBruteForce()

    heights_after_removal = solution.treeQueries(root, queries)
    # heights_after_removal_brute_force = solution_brute_force.treeQueries(root, queries)

    print("Heights after removing subtrees: ", heights_after_removal)
    # print("Heights after removing subtrees using brute force: ", heights_after_removal_brute_force)

if __name__ == "__main__":
    main()