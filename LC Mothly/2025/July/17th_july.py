# Find the Maximum Length of Valid Subsequence II LC 3202

nums=[1,2,3,4,5]
k=2

def maximumLength(nums,k):
    dp=[[0]*k for _ in range(k)]
    l1=1
    for num in nums:
        cur=num % k
        for mod in range(k):
            prev=(mod-cur+k)%k 
            dp[cur][mod]=max(dp[cur][mod], dp[prev][mod] + 1)
            l1=max(l1,dp[cur][mod])
    return l1

print(maximumLength(nums, k))  # Output: 5