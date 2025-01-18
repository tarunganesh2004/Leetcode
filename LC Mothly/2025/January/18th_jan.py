# # Minimum Cost to Make at Least One Valid Path in a Grid LC 1368(Hard)

# # Given an m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:

# 1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
# 2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
# 3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
# 4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
# Notice that there could be some signs on the cells of the grid that point outside the grid.

# You will initially start at the upper left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path does not have to be the shortest.

# You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.

# Return the minimum cost to make the grid have at least one valid path.

# Example 1:
# grid=[[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
# Output: 3
# Explanation: You will start at point (0, 0).
# The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
# The total cost = 3.

# Example 2:
# grid=[[1,1,3],[3,2,2],[1,1,4]]
# Output: 0
# Explanation: You can follow the path from (0, 0) to (2, 2).

from collections import deque


grid=[[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]

def minCost(grid):
    m,n=len(grid),len(grid[0])
    directions=[(0,1),(0,-1),(1,0),(-1,0)] # right, left, down, up
    # Map grid values to direction indices
    direction_map={1:(0,1),2:(0,-1),3:(1,0),4:(-1,0)}

    # deque to store the cell coordinates and the cost to reach that cell
    q=deque([(0,0,0)]) # (x,y,cost)
    cost_grid=[[float('inf')]*n for _ in range(m)]
    cost_grid[0][0]=0 # cost to reach 0,0 is 0

    while q:
        cost,i,j=q.popleft()
        if i==m-1 and j==n-1:
            return cost
        
        for d in range(4):
            ni,nj=i+directions[d][0],j+directions[d][1]

            if 0<=ni<m and 0<=nj<n:
                if directions[d]==direction_map[grid[i][j]]:
                    new_cost=cost
                else:
                    new_cost=cost+1

                if new_cost<cost_grid[ni][nj]: # if find a lower cost update
                    cost_grid[ni][nj]=new_cost
                    if new_cost==cost:
                        q.appendleft((new_cost,ni,nj))
                    else:
                        q.append((new_cost,ni,nj))

    return cost_grid[-1][-1]
    

print(minCost(grid)) # 3