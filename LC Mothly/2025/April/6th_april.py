# Largest Divisible Subset LC 368



nums=[1,2,3]

def largestDivisibleSubset(nums):
    nums.sort()
    ans=[]
    dp=[]
    for i in nums:
        dp.append([i])

    for i in range(len(nums)):
        for j in range(i):
            if nums[i]%nums[j]==0 and len(dp[j])>=len(dp[i]):
                dp[i]=dp[j]+[nums[i]]
            
            if len(ans)<len(dp[i]):
                ans=dp[i]
    
    return ans

print(largestDivisibleSubset(nums))