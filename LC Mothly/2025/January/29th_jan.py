# Redundant Connection LC 684

# In a graph, a cycle is a path of edges that starts and ends at the same vertex. A graph is connected if there is a path between any two nodes. A graph that is connected and has no cycles is called a tree.

# Given a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), and with one additional edge added, find the edge that resulted in the tree being a graph with a cycle. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge (u, v) should be in the same format, with u < v.


edges=[[1,2],[1,3],[2,3]]
# the one that shows up last should be removed to make the graph a tree, i.e [2,3]

# Approach is Union-Find(checking if an edge creates a cycle)
class DSU:
    def __init__(self,n):
        self.parent=[i for i in range(n+1)]
        self.rank=[1]*(n+1)

    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        rootX=self.find(x)
        rootY=self.find(y)
        if rootX==rootY:
            return False # cycle detected
        if self.rank[rootX]>self.rank[rootY]:
            self.parent[rootY]=rootX
        elif self.rank[rootX]<self.rank[rootY]:
            self.parent[rootX]=rootY
        else:
            self.parent[rootY]=rootX
            self.rank[rootX]+=1

        return True

def findRedundantConnection(edges):
    dsu=DSU(len(edges))
    for u,v in edges:
        if not dsu.union(u,v):
            return [u,v]
        
print(findRedundantConnection(edges)) # [2,3]
