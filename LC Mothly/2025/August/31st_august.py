# August 31st LeetCode Challenge
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

def solveSudoku(board):
    # def isValid(board, row, col, num):
    #     for i in range(9):
    #         if board[row][i] == num:
    #             return False
    #         if board[i][col] == num:
    #             return False
    #         if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
    #             return False
    #     return True

    # def solve(board):
    #     for i in range(9):
    #         for j in range(9):
    #             if board[i][j] == ".":
    #                 for num in map(str, range(1, 10)):
    #                     if isValid(board, i, j, num):
    #                         board[i][j] = num
    #                         if solve(board):
    #                             return True
    #                         board[i][j] = "."
    #                 return False
    #     return True

    # solve(board)
    # return board

    row_set=[set() for i in range(9)]
    col_set=[set() for i in range(9)]
    box_set=[[set() for j in range(3)] for i in range(3)]
    for i in range(9):
        for j in range(9):
            if board[i][j]!=".":
                row_set[i].add(board[i][j])
                col_set[j].add(board[i][j])
                box_set[i//3][j//3].add(board[i][j])
    def startFilling(i,j):
        if i==8 and j==9:
            return True 
        if j==9:
            return startFilling(i+1,0)
        
        if board[i][j]!=".":
            return startFilling(i,j+1)
        
        for n in range(1,10):
            if str(n) not in row_set[i] and str(n) not in col_set[j] and str(n) not in box_set[i//3][j//3]:
                board[i][j]=str(n)
                row_set[i].add(str(n))
                col_set[j].add(str(n))
                box_set[i//3][j//3].add(str(n))

                if startFilling(i,j+1):
                    return True 
                
                # backtrack
                board[i][j]="."
                row_set[i].remove(str(n))
                col_set[j].remove(str(n))
                box_set[i//3][j//3].remove(str(n))
                board[i][j]="."
        return False 

    startFilling(0,0)
    return board

print(solveSudoku(board))