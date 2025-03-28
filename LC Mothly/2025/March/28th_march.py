# Maximum Number of Points from Grid Queries LC 2503

grid=[[1,2,3],[2,5,7],[3,5,1]]
queries = [5,6,2]

def maxPoints(grid, queries):
    import heapq
    m=len(grid)
    n=len(grid[0])

    sq=sorted(queries)
    h={}
    vs=set()
    vs.add((0,0))

    pq=[(grid[0][0],0,0)]
    for i in sq:
        while pq:
            v,a,b=pq[0]
            if v>=i:
                break
            heapq.heappop(pq)
            for c,d in (a-1,b),(a+1,b),(a,b-1),(a,b+1):
                if c<0 or c>=m or d<0 or d>=n :
                    continue
                if (c,d) in vs:
                    continue
                heapq.heappush(pq,(grid[c][d],c,d))
                vs.add((c,d))
        h[i]=len(vs)-len(pq)
    return [h[i] for i in queries]

print(maxPoints(grid, queries))