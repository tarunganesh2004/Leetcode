# Number of Ways to Arrive at Destination LC 1976

n=7
roads=[[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]

def countPaths(n,roads):
    import heapq
    from heapq import heappush,heappop
    MOD=10**9+7

    adj=[[] for _ in range(n)]
    for src,dst,timeNeeded in roads:
        adj[src].append((dst,timeNeeded))
        adj[dst].append((src,timeNeeded))

    dist=[float('inf')]*n
    ways=[0]*n
    dist[0]=0
    ways[0]=1
    pq=[]
    heappush(pq,(0,0))

    while pq:
        timeTaken,src=heappop(pq)

        if timeTaken>dist[n-1]:
            continue

        for nei,timeNeeded in adj[src]:
            totalTime=timeTaken+timeNeeded
            if totalTime<dist[nei]:
                ways[nei]=ways[src]
                dist[nei]=totalTime
                heappush(pq,(totalTime,nei))
            elif totalTime==dist[nei]:
                ways[nei]=(ways[nei]+ways[src])%MOD
            

    return ways[n-1]

print(countPaths(n,roads))