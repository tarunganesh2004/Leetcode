# Minimum Cost Walk in Weighted Graph LC 3108

n=5
edges=[[0,1,7],[1,3,7],[1,2,1]]
query = [[0,3],[3,4]]

# union find
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.weights = [131071] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y, weight):
        xx, yy = self.find(x), self.find(y)
        if self.rank[xx] < self.rank[yy]:
            self.parent[xx] = yy
        else:
            self.parent[yy] = xx
        self.weights[xx] = self.weights[yy] = (
            self.weights[xx] & self.weights[yy] & weight
        )
        if self.rank[xx] == self.rank[yy]:
            self.rank[xx] += 1

    def minimum_cost_of_walk(self, x, y):
        if x == y:
            return 0
        if self.find(x) != self.find(y):
            return -1
        return self.weights[self.find(x)]


class Solution:
    def minimumCost(self, n, edges, query):
        uf = DSU(n)
        for x, y, z in edges:
            uf.union(x, y, z)
        return [uf.minimum_cost_of_walk(x, y) for x, y in query]
    
sol=Solution()
print(sol.minimumCost(n,edges,query))
