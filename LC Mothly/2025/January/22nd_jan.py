# # Map of Highest Peak LC 1765

# You are given an integer matrix isWater of size m x n that represents a map of land and water cells.

# If isWater[i][j] == 0, cell (i, j) is a land cell.
# If isWater[i][j] == 1, cell (i, j) is a water cell.
# You must assign each cell a height in a way that follows these rules:

# The height of each cell must be non-negative.
# If the cell is a water cell, its height must be 0.
# Any two adjacent cells must have an absolute height difference of at most 1. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).
# Find an assignment of heights such that the maximum height in the matrix is maximized.

# Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. If there are multiple solutions, return any of them.

from collections import deque


arr=[[0,1],[0,0]]

# The idea is to use BFS to traverse the matrix and assign the height to each cell. We will start with the water cells and assign them height 0. Then we will traverse the matrix and assign the height to the land cells. We will assign the height to the land cell as the maximum height of its adjacent cells + 1. We will keep track of the maximum height assigned to any cell and return the matrix.
def highestPeak(arr):
    dx=[0,0,1,-1] # right, left, down, up
    dy=[1,-1,0,0] # vertical movements corresponding to dx

    rows=len(arr)
    cols=len(arr[0])

    # Initialize the height matrix with -1
    cell_height=[[-1 for i in range(cols)] for j in range(rows)]

    # Queue to perform BFS
    cell_queue=deque()
    
    # add all water cells to the queue and set their height to 0
    for x in range(rows):
        for y in range(cols):
            if arr[x][y]==1:
                cell_queue.append((x,y))
                cell_height[x][y]=0

    # initial height for land cells adjacent to water cells
    height_of_next_layer=1

    while cell_queue:
        layer_size=len(cell_queue)
        for _ in range(layer_size):
            cur_cell=cell_queue.popleft()
            for d in range(4):
                next_x=cur_cell[0]+dx[d]
                next_y=cur_cell[1]+dy[d]
                if next_x>=0 and next_x<rows and next_y>=0 and next_y<cols and cell_height[next_x][next_y]==-1:
                    cell_height[next_x][next_y]=height_of_next_layer
                    cell_queue.append((next_x,next_y))
        height_of_next_layer+=1
    return cell_height

print(highestPeak(arr))