# Set Matrix Zeroes LC 73

mat=[[1,1,1],[1,0,1],[1,1,1]]

def setZeroes(matrix):
    m=len(matrix)
    n=len(matrix[0])
    rowZero=[False]*m
    colZero=[False]*n

    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                rowZero[i]=True
                colZero[j]=True

    for i in range(m):
        for j in range(n):
            if rowZero[i] or colZero[j]:
                matrix[i][j]=0

    return matrix

print(setZeroes(mat))