# Trapping Rain Water II LC 407

# Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

# Example 1:

# heightMap = [[1, 4, 3, 1, 3, 2], 
#              [3, 2, 1, 3, 2, 4], 
#              [2, 3, 3, 2, 3, 1]]

# water cannot be trapped at the edges, because it would just flow out
# water can be trapped at the inner cells

# (1,4,3,1,3,2)  <- Top row
# (3, , , , ,4)  <- Left and right edges
# (2,3,3,2,3,1)  <- Bottom row

#   X   X   X   X   X   X  
#   X  (2) (1)  3  (2)  X  
#   X   X   X   X   X   X  

# (2,1,2) are surrounded by higher terrain,meaning water can be trapped here
# at (1,1) height=2,water trapped=max(0,3-2)=1
# at (1,2) height=1,water trapped=max(0,3-1)=2
# at (1,4) height=2,water trapped=max(0,3-2)=1
# so total water trapped=1+2+1=4

import heapq

heightMap = [[1, 4, 3, 1, 3, 2],
             [3, 2, 1, 3, 2, 4],
             [2, 3, 3, 2, 3, 1]]

# Approach:
# The idea is to use Priority queue+ BFS to find the minimum height cell at the boundary and then traverse the cells inwards to find the water trapped.
# 1)push all boundary cells into a minheap(since they cant hold water)
# 2)expand from the smallest boundary cell(like BFS)
# check its neighbors, if the neighbor is smaller than the current cell, then water can be trapped at the neighbor cell
# push the neighbor cell into the heap and update the height of the neighbor cell to the current cell height
# 3)repeat until all cells are visited

def trapRainWaterII(heightMap): # O(m*n*log(m*n)), log(m*n) to push and pop from heap, m*n to visit all cells, and space complexity is O(m*n)
    if not heightMap or not heightMap[0]:
        return 0
    
    rows,cols=len(heightMap),len(heightMap[0])
    visited=[[False]*cols for _ in range(rows)]
    heap=[]

    # push all boundary cells into the heap
    for i in range(rows):
        for j in range(cols):
            if i==0 or j==0 or i==rows-1 or j==cols-1:
                heapq.heappush(heap,(heightMap[i][j],i,j))
                visited[i][j]=True

    directions=[(0,1),(0,-1),(1,0),(-1,0)] # right, left, down, up
    trapped_water=0

    while heap:
        height,r,c=heapq.heappop(heap)
        for dr,dc in directions:
            nr,nc=r+dr,c+dc

            if 0<=nr<rows and 0<=nc<cols and not visited[nr][nc]:
                visited[nr][nc]=True

                # if neighbor is lower then trap water
                if height>heightMap[nr][nc]:
                    trapped_water+=height-heightMap[nr][nc]
                
                # push the neighbor cell into the heap
                heapq.heappush(heap,(max(height,heightMap[nr][nc]),nr,nc))

    return trapped_water

print(trapRainWaterII(heightMap)) # 4