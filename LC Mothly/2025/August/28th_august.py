# Sort Matrix By Diagonals LC 3446

grid=[[1,7,3],[9,8,2],[4,5,6]]

def sortMatrix(grid):
    n=len(grid)

    # diagonal id = i-j, if i>=j-->bottom left including main diagonal
    # if i<j-->top right excluding main diagonal

    diag_map={}
    for i in range(n):
        for j in range(n):
            key=i-j
            if key not in diag_map:
                diag_map[key]=[]
            diag_map[key].append(grid[i][j])

    # sort each diagonal
    for key in diag_map:
        if key>=0: # bottom left
            diag_map[key].sort(reverse=True) # sort in descending order
        else: # top -right
            diag_map[key].sort() # sort in ascending order
    
    # write back to the grid 
    for i in range(n):
        for j in range(n):
            key=i-j
            grid[i][j]=diag_map[key].pop(0) # pop(0) means take from front in order
    
    return grid

print(sortMatrix(grid))