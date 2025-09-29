# Minimum Score Triangulation of Polygon LC 1039

values = [1,3,1,4,1,5]

def minScoreTriangulation(values):
    n = len(values)
    dp=[[0 for i in range(n)] for j in range(n)]

    for k in range(2,n):
        for j in range(n-k):
            start,end=j,j+k
            dp[start][end]=float('inf') # type: ignore
            for i in range(start+1,end):
                dp[start][end]=min(dp[start][end],dp[start][i]+dp[i][end]+values[start]*values[i]*values[end])
    return dp[0][n-1]

print(minScoreTriangulation(values))