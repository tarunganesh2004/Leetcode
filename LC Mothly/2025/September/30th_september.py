# Find Triangular Sum of an Array LC 2221

nums=[1,2,3,4,5]

def otherWay(nums):
    for i in range(len(nums)-1,-1,-1):
        for j in range(i):
            nums[j]=(nums[j]+nums[j+1])%10
    return nums[0]

def triangularSum(nums):
    n=len(nums)
    dp=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        dp[i][i]=nums[i]
    
    for k in range(1,n):
        for j in range(n-k):
            start,end=j,j+k
            dp[start][end]=(dp[start][end-1]+dp[start+1][end])%10
    return dp[0][n-1]

print(triangularSum(nums))
print(otherWay(nums))