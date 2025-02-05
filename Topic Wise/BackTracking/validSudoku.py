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


def isValidSudoku(board): # TC and SC is O(1)
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

def anotherWay(board): 
    # using only single set
    seen=set()
    for i in range(9):
        for j in range(9):
            num=board[i][j]

            if num==".":
                continue

            row_num=(num,i)
            col_num=(j,num)
            subgrid_num=(i//3,j//3,num)

            if row_num in seen or col_num in seen or subgrid_num in seen:
                return False

            seen.add(row_num)
            seen.add(col_num)
            seen.add(subgrid_num)
    return True


print(isValidSudoku(board)) # True

print(anotherWay(board)) # True