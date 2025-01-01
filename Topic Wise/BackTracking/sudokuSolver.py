# Sudoku Solver LC 37

board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

# def solveSudoku(board): # TLE(6/7)
#     # check if the number is valid in the board
#     def isValid(r,c,num):
#         num=str(num)
#         for i in range(9):
#             if board[i][c]==num or board[r][i]==num:
#                 return False
#             if board[3*(r//3)+i//3][3*(c//3)+i%3]==num:
#                 return False
            
#         return True
    
#     def backtrack(board):
#         for i in range(9):
#             for j in range(9):
#                 if board[i][j]==".":
#                     for num in range(1,10):
#                         if isValid(i,j,num):
#                             board[i][j]=str(num)
#                             if backtrack(board):
#                                 return True
#                             board[i][j]="."
#                     return False
#         return True
    
#     backtrack(board)

def solveSudoku(board):
    # use sets to store the numbers in the row, column and subgrid
    row=[set() for _ in range(9)]
    col=[set() for _ in range(9)]
    subgrid=[set() for _ in range(9)]
    empty_cells=[] # store the empty cells

    # fill the sets with the numbers in the board
    for r in range(9):
        for c in range(9):
            if board[r][c]==".":
                empty_cells.append((r,c))
            else:
                num=board[r][c]
                row[r].add(num)
                col[c].add(num)
                subgrid[(r//3)*3+c//3].add(num) # 3x3 subgrid

    def isValid(r,c,num):
        subgrid_index=(r//3)*3+c//3
        return num not in row[r] and num not in col[c] and num not in subgrid[subgrid_index]
    
    def backtrack(index):
        if index==len(empty_cells):
            return True
        
        r,c=empty_cells[index]
        for num in "123456789":
            if isValid(r,c,num):
                # place the number
                board[r][c]=num
                row[r].add(num)
                col[c].add(num)
                subgrid[(r//3)*3+c//3].add(num)

                # recur to the next empty cell
                if backtrack(index+1):
                    return True
                
                # backtrack and remove the number
                board[r][c]="."
                row[r].remove(num)
                col[c].remove(num)
                subgrid[(r//3)*3+c//3].remove(num)

        return False
    
    backtrack(0)

solveSudoku(board)
print(board)