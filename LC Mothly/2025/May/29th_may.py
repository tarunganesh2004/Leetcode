# Maximize the Number of Target Nodes after Connecting Trees II LC 3373(Hard)

from collections import deque


edges1 = [[0,1],[0,2],[2,3],[2,4]]
edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]

def maxTargetNodes(edges1, edges2):
    def find_even(edges,n):
        graph=[[] for _ in range(n)]
        queue=deque([(0,-1,True)]) # (node,parent,is_even)
        evens=[False]*n

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        while queue:
            node, parent, is_even = queue.popleft()
            evens[node] = is_even
            
            for neighbor in graph[node]:
                if neighbor != parent:
                    queue.append((neighbor, node, not is_even)) # type: ignore
        return evens
    
    n = len(edges1) + 1
    m = len(edges2) + 1
    evens1 = find_even(edges1, n)
    evens2 = find_even(edges2, m)
    sm1,sm2=sum(evens1), sum(evens2)
    mx=max(sm2, m - sm1)
    ans=[mx+(sm1 if even else n-sm1) for even in evens1]
    return ans

print(maxTargetNodes(edges1, edges2))
    