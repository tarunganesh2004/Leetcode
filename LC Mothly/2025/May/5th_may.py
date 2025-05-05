# Domino and Tromino Tiling LC 790

n=3

def numTilings(n):
    dp=[1,2,5]+[0]*n
    for i in range(3, n+1):
        dp[i]= (2*dp[i-1]+dp[i-3])%1000000007
    return dp[n-1]

print(numTilings(n))  # Output: 5