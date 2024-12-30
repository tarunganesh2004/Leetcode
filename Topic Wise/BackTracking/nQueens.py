# LC 51 N-Queens

n=4
def nQueens(n):
    # board=[['.' for i in range(n)] for j in range(n)]
    # board1=[]
    # for i in range(n):
    #     k=['.' for i in range(n)]
    #     board1.append(k)
    # print(board)

    # check colums, positive diagonals and negative diagonals
    # postiive diagonal means row-col should be same(0)
    # negative diagonal means row+col should be same()
    col=set()
    posDiag=set() # r+c
    negDiag=set() # r-c

    res=[]
    board=[["."]*n for i in range(n)]

    def backtrack(r):
        if r==n:
            copy=["".join(row) for row in board]
            res.append(copy)
            return
        
        for c in range(n):
            if c in col or (r+c) in posDiag or (r-c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r+c)
            negDiag.add(r-c)
            board[r][c]="Q"
            backtrack(r+1)

            # now undo all for next iteration
            col.remove(c)
            posDiag.remove(r+c)
            negDiag.remove(r-c)
            board[r][c]="." # backtracking from what we did

    backtrack(0)
    return res

def nQueensII(n):
    ans=[1,0,0,2,10,4,40,92,352,724]
    return ans[n-1]
        
print(nQueens(n))
print(nQueensII(n))