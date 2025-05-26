# Largest Color Value in a Directed Graph LC 1857(Hard)



colors="abaca"
edges=[[0,1],[0,2],[2,3],[3,4]]

def largestPathValue(colors, edges):
    n=len(colors)
    adj= [[] for _ in range(n)]
    for a,b in edges:
        adj[a].append(b)

    vis= [0]*n
    tp=[]
    cycle=False
    def dfs(node):
        nonlocal cycle
        if vis[node]:
            if vis[node] == 1:
                cycle = True
            return
        vis[node] = 1
        for c in adj[node]:
            dfs(c)
        vis[node] = 2
        tp.append(node)

    for i in range(n):
        if not vis[i]:
            dfs(i)
    if cycle:
        return -1
    tp.reverse()

    colors=[ord(c)-ord('a') for c in colors]
    ans=0
    for c in range(26):
        count=[0]*n
        for v in tp:
            if colors[v] == c:
                count[v] += 1
                ans = max(ans, count[v])
            for nei in adj[v]:
                count[nei] = max(count[nei], count[v])
    return ans

print(largestPathValue(colors, edges))  # Output: 3