# # Surrounded Regions LC 130

# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

board=[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# the approach is to first find the 'O's on the edge of the board and then do dfs on those 'O's and mark them as 'Y'
# then iterate through the board and mark all the 'O's as 'X' and 'Y's as 'O'
def solve(board):
    n=len(board)
    m=len(board[0])
    vis=[[0 for i in range(m)] for j in range(n)]

    dir=[[0,1],[1,0],[0,-1],[-1,0]]

    def dfs(i,j,board,vis):
        if i<0 or j<0 or i>=n or j>=m or vis[i][j]==1 or board[i][j]=='X':
            return
        vis[i][j]=1
        # board[i][j]='Y'
        for d in dir:
            dfs(i+d[0],j+d[1],board,vis)
        
    
    # traverse the first and last row
    for j in range(m):
        # first row
        if vis[0][j]==0 and board[0][j]=='O':
            dfs(0,j,board,vis)

        # last row
        if vis[n-1][j]==0 and board[n-1][j]=='O':
            dfs(n-1,j,board,vis)

    
    # traverse the first and last column
    for i in range(n):
        # first column
        if vis[i][0]==0 and board[i][0]=='O':
            dfs(i,0,board,vis)

        # last column
        if vis[i][m-1]==0 and board[i][m-1]=='O':
            dfs(i,m-1,board,vis)

    for i in range(n):
        for j in range(m):
            if board[i][j]=='O'and vis[i][j]==0:
                board[i][j]='X'
    return board

print(solve(board))