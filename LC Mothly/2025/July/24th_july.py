# Minimum Score After Removals on a Tree 

from collections import defaultdict


nums=[1,5,5,4,11]
edges=[[0,1],[1,2],[1,3],[3,4]]

def minimumScore(nums, edges):
    n=len(nums)
    tree=defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    parent=[-1]*n
    xor= [0]*n
    in_time=[0]*n
    out_time=[0]*n
    time=[0]

    def dfs(node, par):
        parent[node]= par
        xor[node] = nums[node]
        time[0] += 1
        in_time[node] = time[0]

        for neighbor in tree[node]:
            if neighbor!=par:
                dfs(neighbor, node)
                xor[node] ^= xor[neighbor]
        time[0] += 1
        out_time[node] = time[0]
    
    dfs(0, -1)
    total_xor= xor[0]

    def is_ancestor(u, v):
        return in_time[u] < in_time[v] and out_time[u] > out_time[v]
    
    edge_nodes= []
    for u,v in edges:
        if parent[v]==u:
            edge_nodes.append(v)
        else:
            edge_nodes.append(u)
    
    ans= float('inf')

    for i in range(len(edge_nodes)):
        for j in range(i+1,len(edge_nodes)):
            a= edge_nodes[i]
            b= edge_nodes[j]

            if is_ancestor(a, b):
                xor1=xor[b]
                xor2=xor[a] ^ xor[b]
                xor3= total_xor ^ xor[a]
            elif is_ancestor(b, a):
                xor1=xor[a]
                xor2=xor[b] ^ xor[a]
                xor3= total_xor ^ xor[b]
            else:
                xor1=xor[a]
                xor2=xor[b]
                xor3= total_xor ^ xor[a] ^ xor[b]
            
            scores= [xor1, xor2, xor3]
            ans=min(ans, max(scores) - min(scores))
    return ans

print(minimumScore(nums, edges)) 