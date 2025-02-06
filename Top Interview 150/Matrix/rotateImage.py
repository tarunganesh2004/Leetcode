# Rotate Image LC 48

mat=[[1,2,3],[4,5,6],[7,8,9]]

def rotateImage(mat):
    n=len(mat)
    for i in range(n):
        for j in range(i+1,n):
            mat[i][j],mat[j][i]=mat[j][i],mat[i][j]

    for row in mat:
        row.reverse()

    return mat

print(rotateImage(mat))