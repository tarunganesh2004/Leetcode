# Count Submatrices with all ones LC 1504

mat=[[1,0,1],
      [1,1,0],
      [1,1,0]]

def numSubmat(mat):
    m,n,res= len(mat), len(mat[0]), 0

    histogram=[0]*(n+1)
    for i in range(m):
        stack,dp=[-1], [0]*(n+1)
        for j in range(n):
            if mat[i][j]==0:
                histogram[j]=0
            else:
                histogram[j]+=1

            while histogram[j]<histogram[stack[-1]]:
                stack.pop()
            dp[j]=dp[stack[-1]]+histogram[j]*(j-stack[-1])
            stack.append(j)
        res+=sum(dp)
    return res

print(numSubmat(mat))  # Output: 13