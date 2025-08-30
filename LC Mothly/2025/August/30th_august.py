# Valid Sudoku

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

def isValidSudoku(board):
    seen=set()
    for i in range(9):
        for j in range(9):
            num=board[i][j]

            if num==".":
                continue 

            row_num=(i,num)
            col_num=(num,j)
            subgrid_num=(i//3,j//3,num)

            if row_num in seen or col_num in seen or subgrid_num in seen:
                return False
            
            seen.add(row_num)
            seen.add(col_num)
            seen.add(subgrid_num)

    return True

print(isValidSudoku(board))