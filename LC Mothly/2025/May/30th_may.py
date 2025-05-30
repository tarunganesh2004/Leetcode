# Find Closest Node to Given Two Nodes LC 2359

edges=[2,2,3,-1]
node1=0
node2=1

def closestMeetingNode(edges,node1,node2):
    def dfs(node,adj,vis,dist):
        vis[node] = True
        for nei in adj[node]:
            if not vis[nei]:
                dist[nei] = dist[node] + 1
                dfs(nei, adj, vis, dist)

    n = len(edges)
    adj = [[] for _ in range(n)]
    for i in range(n):
        if edges[i] != -1:
            adj[i].append(edges[i])
    
    vis1 = [False] * n
    vis2 = [False] * n
    dist1 = [0] * n
    dist2 = [0] * n

    dfs(node1, adj, vis1, dist1)
    dfs(node2, adj, vis2, dist2)
    min_dist = float('inf')
    ans = -1

    for i in range(n):
        if vis1[i] and vis2[i]:
            max_dist = max(dist1[i], dist2[i])
            if max_dist < min_dist:
                min_dist = max_dist
                ans = i
    return ans

print(closestMeetingNode(edges, node1, node2))  # Output: 2
