# Delete Duplicate Folders in System LC 1948(Hard)

from collections import defaultdict


paths = [["a"], ["c"], ["d"], ["a", "b"], ["c", "b"], ["d", "a"]]

class TrieNode:
    def __init__(self):
        self.child=defaultdict(TrieNode)
        self.deleted=False
    
    def addWord(self,word):
        cur=self 
        for c in word:
            cur=cur.child[c]
        
class Solution:
    def deleteDuplicateFolder(self, paths):
        def serialize(root,seen):
            if not root.child:
                return ""
            keys=[]
            for c,child in root.child.items():
                keys.append(c+":"+serialize(child,seen))
            key="("+"".join(keys)+")"
            seen[key].append(root)
            return key
        
        def dfsGetValidPaths(root, path, out):
            for c, child in root.child.items():
                if not child.deleted:
                    out.append(path + [c])
                    dfsGetValidPaths(child, path + [c], out)

        trieRoot, seen = TrieNode(), defaultdict(list)
        # Create graph
        for path in sorted(
            paths
        ):  # Sort paths to get correct orders of children of a subtree
            trieRoot.addWord(path)

        # Find duplicated subtrees
        serialize(trieRoot, seen)

        # Mark duplicated subtree nodes as deleted
        for nodes in seen.values():
            if len(nodes) >= 2:
                for node in nodes:  # Mark duplicated subtrees as deleted
                    node.deleted = True

        ans = []
        dfsGetValidPaths(trieRoot, [], ans)
        return ans
    
solution = Solution()
print(solution.deleteDuplicateFolder(paths))  # Output: [["d"],["d","a"]]