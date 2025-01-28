# Number of Islands LC 200

from collections import deque


grid=[
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]

def numIslands(grid):
    if not grid:
        return 0
    
    def dfs(grid, i, j):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]=="0":
            return
        grid[i][j]="0"
        dfs(grid, i+1, j)
        dfs(grid, i-1, j)
        dfs(grid, i, j+1)
        dfs(grid, i, j-1)
    
    count=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=="1":
                dfs(grid, i, j)
                count+=1
    return count

# Another way to solve this problem is by using BFS
def numIslandsBFS(grid):
    if not grid:
        return 0
    r, c = len(grid), len(grid[0])
    count = 0
    q = deque()
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def bfs(i, j):
        q.append((i, j))
        grid[i][j] = "0"  # Mark as visited

        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == "1":
                    grid[nx][ny] = "0"  # Mark as visited
                    q.append((nx, ny))

    for i in range(r):
        for j in range(c):
            if grid[i][j] == "1":  # Found an island
                bfs(i, j)
                count += 1

    return count

# print(numIslands(grid))
print(numIslandsBFS(grid))