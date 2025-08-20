# Count Square Submatrices with all ones LC 1277



matrix=[[0,1,1,1],
         [1,1,1,1],
         [0,1,1,1]]

def countSquares(matrix):
    row,col= len(matrix), len(matrix[0])
    dp=[[0]*(col+1) for _ in range(row+1)]

    ans=0
    for i in range(row):
        for j in range(col):
            if matrix[i][j]:
                dp[i+1][j+1] = min(dp[i][j], dp[i][j+1], dp[i+1][j]) + 1
                ans += dp[i+1][j+1]
                print(f"Updated dp[{i+1}][{j+1}] to {dp[i+1][j+1]}, current ans: {ans}")
    return ans

print(countSquares(matrix))  # Output: 15