# Minimum Operations to Make a Uni-Value Grid LC 2033

grid=[[2,4],[6,8]]
x=2

def minOperations(grid,x):
    from collections import defaultdict
    M,n=len(grid),len(grid[0])

    d=defaultdict(int)
    medianIdx=(M*n)//2
    for i in range(M):
        for j in range(n):
            d[grid[i][j]]+=1

    keys=sorted(d)
    cur=median=0

    for k in keys:
        cur+=d[k]
        if cur>medianIdx:
            median=k
            break
    res=0
    for k in d:
        cnt=abs(k-median)/x
        if cnt%1!=0:
            return -1
        res+=d[k]*cnt
    return int(res)

print(minOperations(grid,x))