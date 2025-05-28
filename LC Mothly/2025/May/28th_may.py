# Maximize the Number of Target Nodes after Connecting Trees I LC 3372

from collections import defaultdict, deque


edges1 = [[0,1],[0,2],[2,3],[2,4]]
edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
k = 2

def maxTargetNodes(edges1, edges2, k):
    def build_graph(edges):
        graph=defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph
    graph1 = build_graph(edges1)
    graph2 = build_graph(edges2)
    n,m=len(edges1)+1, len(edges2)+1

    def bfs_count(map,start,max_depth):
        vis=[False]*(max(map.keys())+1)
        q=deque([(start, 0)])
        count=0
        while q:
            node, depth = q.popleft()
            if vis[node] or depth > max_depth:
                continue
            vis[node] = True
            count += 1
            for neighbor in map[node]:
                if not vis[neighbor]:
                    q.append((neighbor, depth + 1))
        return count
    
    cal1=[bfs_count(graph1, i, k) for i in range(n)]
    cal2=max(bfs_count(graph2, i, k-1) for i in range(m))

    return [cal1[i]+cal2 for i in range(n)]

print(maxTargetNodes(edges1, edges2, k))