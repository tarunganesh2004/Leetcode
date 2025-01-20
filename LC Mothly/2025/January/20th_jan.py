# # First Completely Painted Row or Column LC 2661

# You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].

# Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].

# Return the smallest index i at which either a row or a column will be completely painted in mat.

arr=[1,3,4,2]
mat=[[1,4],[2,3]]

def isCompleted(mat,r,c,m,n):
    rowC=True
    for j in range(n):
        if mat[r][j]==0:
            rowC=False
            break
    colC=True
    for j in range(m):
        if mat[j][c]==0:
            colC=False
            break
    return rowC or colC
# bruteforce approach:
def firstCompleteIndexBrute(arr,mat): # O(m*n*len(arr)), m*n to find the index of the element in the matrix, len(arr) to find the index of the element in the array
    m=len(mat)
    n=len(mat[0])
    dummy=[[0]*n for _ in range(m)]
    for i in range(len(arr)):
        r,c=-1,-1
        for j in range(m):
            for k in range(n):
                if mat[j][k]==arr[i]:
                    dummy[j][k]=1
                    r,c=j,k
                    break
            if r!=-1:
                break

        if isCompleted(dummy,r,c,m,n):
            return i
    return -1

# So the optimized approach is to use hashmap to store the positions of each number in the matrix
# and track the count of each row and column

def firstCompleteIndex(arr,mat):
    m,n=len(mat),len(mat[0])
    # hashmap to store the positions of each number in the matrix
    pos={}
    for i in range(m):
        for j in range(n):
            pos[mat[i][j]]=(i,j)
    
    rowCount=[0]*m
    colCount=[0]*n
    for i,num in enumerate(arr):
        r,c=pos[num]
        rowCount[r]+=1
        colCount[c]+=1

        if rowCount[r]==n or colCount[c]==m:
            return i
    return -1

print(firstCompleteIndexBrute(arr,mat)) # 2

print(firstCompleteIndex(arr,mat))