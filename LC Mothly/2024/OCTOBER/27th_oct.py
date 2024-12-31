# LC 1277 Count square submatrices with all ones
 # approach
# choose (i,j) as the bottom right corner of the square matrix
# if matrix[i][j]==1 then the number of square matrices with (i,j) as the bottom right corner is 1
# Find maximal square size ending at all cells (i,j)
# add all size values 

m=[[0,1,1,1],[1,1,1,1],[0,1,1,1]]


# extending square size : maximal square size ending at (i,j) is the minimum of the square sizes ending at (i-1,j),(i,j-1),(i-1,j-1) +1
def count_submatrices(mat):

    # finding the maximal square size ending at (i,j)

    m,n=len(mat),len(mat[0])

    maximal_square_size=[[0]*(n+1) for _ in range(m+1)]

    square_submatrices=0
    for i in range(1,m+1):
        for j in range(1,n+1):

            if mat[i-1][j-1]==1:
                maximal_square_size[i][j]=1+min(maximal_square_size[i-1][j],maximal_square_size[i][j-1],maximal_square_size[i-1][j-1])
                square_submatrices+=maximal_square_size[i][j]

    return square_submatrices # TC O(m*n) SC O(m*n)

print(count_submatrices(m)) # 15