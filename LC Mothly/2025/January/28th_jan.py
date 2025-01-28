# # Maximum Number of Fish in a Grid LC 2658
# You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

# A land cell if grid[r][c] = 0, or
# A water cell containing grid[r][c] fish, if grid[r][c] > 0.
# A fisher can start at any water cell (r, c) and can do the following operations any number of times:

# Catch all the fish at cell (r, c), or
# Move to any adjacent water cell.
# Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

# An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

from collections import deque


grid=[
    [0,2,1,0],
    [4,0,0,3],
    [1,0,0,4],
    [0,3,2,0]
]

def findMaxFish(grid): # O(m*n) time and O(m*n) space
    r,c=len(grid),len(grid[0])
    res=0
    visited=[[False]*c for _ in range(r)]
    def countFish(grid,i,j,vis):
        fish_count=0
        q=deque([(i,j)])
        vis[i][j]=True
        # directions
        dirs=[(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            x,y=q.popleft()
            fish_count+=grid[x][y]
            for dx,dy in dirs:
                nx,ny=x+dx,y+dy
                if 0<=nx<r and 0<=ny<c and grid[nx][ny] and not vis[nx][ny]:
                    vis[nx][ny]=True
                    q.append((nx,ny))
        return fish_count
    for i in range(r):
        for j in range(c):
            if grid[i][j] and not visited[i][j]:
                res=max(res,countFish(grid,i,j,visited))
    return res

# using dfs
def findMaxFishDFS(grid): # O(m*n) time and O(m*n) space
    r,c=len(grid),len(grid[0])
    res=0
    visited=[[False]*c for _ in range(r)]
    def countFish(grid,i,j,vis):
        fish_count=grid[i][j]
        vis[i][j]=True
        # directions
        dirs=[(0,1),(0,-1),(1,0),(-1,0)]
        for dx,dy in dirs:
            nx,ny=i+dx,j+dy
            if 0<=nx<r and 0<=ny<c and grid[nx][ny] and not vis[nx][ny]:
                fish_count+=countFish(grid,nx,ny,vis)
        return fish_count
    for i in range(r):
        for j in range(c):
            if grid[i][j] and not visited[i][j]:
                res=max(res,countFish(grid,i,j,visited))
    return res

print(findMaxFish(grid)) # 7
print(findMaxFishDFS(grid)) # 7