# # Rotting Oranges LC 994

# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

from collections import deque


grid=[[2,1,1],[1,1,0],[0,1,1]]

# the approach is to first find the rotten oranges and then do bfs on the rotten oranges and keep track of the fresh oranges that are rotten
# if at the end there are fresh oranges left then return -1 else return the time taken to rot all the fresh oranges

def orangesRotting(grid):
    n=len(grid)
    m=len(grid[0])
    q=deque()
    vis=[[0 for i in range(m)] for j in range(n)]
    cntFresh=0
    for i in range(n):
        for j in range(m):
            if grid[i][j]==2:
                q.append((i,j,0))
                vis[i][j]=2
            else:
                vis[i][j]=0
            if grid[i][j]==1:
                cntFresh+=1
    
    time=0
    count=0
    dir=[[0,1],[1,0],[0,-1],[-1,0]]
    while q:
        r,c,t=q.popleft()
        time=max(time,t)
        for d in dir:
            x=r+d[0]
            y=c+d[1]
            if x>=0 and y>=0 and x<n and y<m and vis[x][y]==0 and grid[x][y]==1:
                vis[x][y]=2
                q.append((x,y,t+1))
                count+=1

    if count==cntFresh:
        return time
    else:
        return -1
    
print(orangesRotting(grid))
