# Diagonal Traverse LC 498



mat=[[1,2,3],[4,5,6],[7,8,9]]

def findDiagonalOrder(mat):
    d={}
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i+j not in d:
                d[i+j]=[mat[i][j]]
            else:
                d[i+j].append(mat[i][j])
    
    res=[]
    for entry in d.items():
        if entry[0]%2==0:
            [res.append(x) for x in entry[1][::-1]]
        else:
            [res.append(x) for x in entry[1]]
    return res

print(findDiagonalOrder(mat))