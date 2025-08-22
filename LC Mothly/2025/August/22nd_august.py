# Find the Minimum Area to Cover All Ones I LC 3195

grid=[[0,1,0],[1,0,1]]

def minimumArea(grid):
    m,n=len(grid),len(grid[0])
    minRow,maxRow=m,-1
    minCol,maxCol=n,-1
    for i in range(m):
        for j in range(n):
            if grid[i][j]==1:
                minRow=min(minRow,i)
                maxRow=max(maxRow,i)
                minCol=min(minCol,j)
                maxCol=max(maxCol,j)
    
    return (maxRow-minRow+1)*(maxCol-minCol+1) 

print(minimumArea(grid))  # Output : 6