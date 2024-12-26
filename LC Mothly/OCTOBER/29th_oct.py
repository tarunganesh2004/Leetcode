# Maximum number of moves in  a grid - LC 2684

# Approach
# so basically we have to find the maximum number of moves that can be made in a grid
# we can move in 4 directions: up,down,left,right

# Initiate BFS from each row in the leftmost column

# allow movements(1,0),(0,1),(-1,0),(0,-1)(up,right,down,left)
# keep count of moves by updating a variable as we explore cells using BFS
# check move validity by ensuring next cell has a higher value than the current cell and hasnt been visited before
# return the maximum count after all possible starting points have been explored

from hmac import new
from typing import List
from collections import deque

class Solution:
    class Pair:
        def __init__(self,x,y,steps):
            self.x=x
            self.y=y
            self.steps=steps
    
    def maxMoves(self,grid:List[List[int]]) -> int: # TC O(m^2*n), SC O(m*n), not optimized
        max_moves=0
        for i in range(len(grid)):
            max_moves=max(max_moves,self.bfs(grid,i,0))
        return max_moves
    
    def bfs(self,grid:List[List[int]],row:int,col:int) -> int:
        queue=deque([self.Pair(row,0,0)])
        m,n=len(grid),len(grid[0])
        visited=[[False]*n for _ in range(m)]
        dir=[(-1,1),(0,1),(1,1)] # up-right, right,down-right
        max_steps=0

        visited[row][0]=True

        while queue:
            p=queue.popleft()
            max_steps=p.steps

            for dx,dy in dir:
                new_x,new_y=p.x+dx,p.y+dy

                if self.is_valid(grid,new_x,new_y,p.x,p.y,visited):
                    queue.append(self.Pair(new_x,new_y,p.steps+1))
                    visited[new_x][new_y]=True

        return max_steps
 
    def is_valid(self,grid:List[List[int]],new_x:int,new_y:int,x:int,y:int,visited:List[List[bool]]) -> bool:
        m,n=len(grid),len(grid[0])
        return 0<=new_x<m and 0<=new_y<n and grid[new_x][new_y]>grid[x][y] and not visited[new_x][new_y]
    
    # We can use recursion but it takes tc O(3^m*n)
    
    # Optimized approach (DP) TC O(m*n), SC O(m*n)
    def maxMovesOptimized(self,grid:List[List[int]]) -> int:
        def dfs(r,c,grid,mem):
            if mem[r][c]!=-1:
                return mem[r][c]
            
            max_moves=0
            # # dir=[(-1,1),(0,1),(1,1)] # up-right, right,down-right
            # if r-1>=0 and c+1<len(grid[0]) and grid[r-1][c+1]>grid[r][c]:
            #     max_moves=1+dfs(r-1,c+1,grid,mem)
            # if c+1<len(grid[0]) and grid[r][c+1]>grid[r][c]:
            #     max_moves=max(max_moves,1+dfs(r,c+1,grid,mem))
            # if r+1<len(grid) and c+1<len(grid[0]) and grid[r+1][c+1]>grid[r][c]:
            #     max_moves=max(max_moves,1+dfs(r+1,c+1,grid,mem))

            dir=[(-1,1),(0,1),(1,1)]
            for dr,dc in dir:
                new_r,new_c=r+dr,c+dc

                if 0<=new_r<len(grid) and 0<=new_c<len(grid[0]) and grid[new_r][new_c]>grid[r][c]:
                    max_moves=max(max_moves,1+dfs(new_r,new_c,grid,mem))
            
            mem[r][c]=max_moves
            return max_moves

        
        rows=len(grid)
        cols=len(grid[0])

        mem=[[-1]*cols for _ in range(rows)]

        max_moves=0
        for i in range(rows):
            max_moves=max(max_moves,dfs(i,0,grid,mem))
        
        return max_moves
s=Solution()
grid = [[2, 4, 3, 5], 
        [5, 4, 9, 3], 
        [3, 4, 2, 11], 
        [10, 9, 13, 15]]
print(s.maxMoves(grid)) # 3 , # (0,0)->(0,1), (0,1)->(1,2), (1,2)->(2,3)

grid1 = [[3, 2, 4], [2, 1, 9], [1, 1, 7]]
print(s.maxMoves(grid1))  
print(s.maxMovesOptimized(grid))
print(s.maxMovesOptimized(grid1)) 