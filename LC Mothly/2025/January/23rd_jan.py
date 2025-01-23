# Count Servers that Communicate LC 1267

# You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

# Return the number of servers that communicate with any other server.

grid=[[1,0],[0,1]] # here there are no servers in same row or column, so the answer is 0

# approach is to use two arrays to store the count of servers in each row and column. Then we will iterate over the matrix and count the servers that communicate with any other server.
def countServers(grid): # O(m*n) time complexity, O(m+n) space complexity
    rows=len(grid)
    cols=len(grid[0])
    row_count=[0]*rows
    col_count=[0]*cols
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]==1:
                row_count[i]+=1
                col_count[j]+=1
    count=0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]==1 and (row_count[i]>1 or col_count[j]>1): # if there are more than 1 servers in the row or column
                count+=1
    return count

print(countServers(grid)) # 0