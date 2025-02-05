# Valid Sudoku LC 36

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]] # type: ignore


def isValidSudoku(board):
    # use sets to store the numbers in the row, column and subgrid
    row=[set() for _ in range(9)]
    col=[set() for _ in range(9)]
    subgrid=[set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            num=board[i][j]

            if num==".":
                continue

            subgrid_idx=(i//3)*3+j//3
            if num in row[i] or num in col[j] or num in subgrid[subgrid_idx]:
                return False
            
            row[i].add(num)
            col[j].add(num)
            subgrid[subgrid_idx].add(num)
    return True

print(isValidSudoku(board)) # True