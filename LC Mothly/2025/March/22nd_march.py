# Count the Number of Complete Components LC 2685

n=6
edges=[[0,1],[0,2],[1,2],[3,4]]

def countCompleteComponents(n,edges):
    from collections import Counter
    graph={i:[i] for i in range(n)}

    ans,conv=0,lambda x:tuple(sorted(x))

    for a,b in edges:
        graph[a].append(b);graph[b].append(a)

    vals=Counter(map(conv,graph.values()))

    return sum(len(edgeList)==vals[edgeList] for edgeList in vals)

print(countCompleteComponents(n,edges))