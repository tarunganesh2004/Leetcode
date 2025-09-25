# Triangle LC 120

from functools import lru_cache


triangle=[[2],[3,4],[6,5,7],[4,1,8,3]]

# brute force recursion
def minPat(triangle,row=0,col=0):
    if row==len(triangle)-1:
        return triangle[row][col]
    
    # move down to the same column in the next row
    left=minPat(triangle,row+1,col)
    # move down to the next column in the next row
    right=minPat(triangle,row+1,col+1)
    return triangle[row][col]+min(left,right)

# now above can be optimized using memoization
def minPathMemo(triangle):
    @lru_cache(None)
    def dfs(r,c):
        if r==len(triangle)-1:
            return triangle[r][c]
        
        left=dfs(r+1,c)
        right=dfs(r+1,c+1)
        return triangle[r][c]+min(left,right)
    return dfs(0,0)

# DP 
def dp(triangle):
    dp=triangle[-1][:]

    # move upwards by row 
    for r in range(len(triangle)-2,-1,-1):
        for c in range(len(triangle[r])):
            # dp[c] is cost from below-left
            # dp[c+1] is cost from below-right
            dp[c]=triangle[r][c]+min(dp[c],dp[c+1])
    return dp[0]

print(minPat(triangle))
print(minPathMemo(triangle))
print(dp(triangle))