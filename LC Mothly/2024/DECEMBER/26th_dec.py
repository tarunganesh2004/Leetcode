# Target Sum LC 494

from collections import defaultdict


def findTargetSumWays(nums,target):
    dp={} # memoization (idx,cur_sum):ways

    def backtrack(idx,cur_sum):
        if (idx,cur_sum) in dp: # if already calculated
            return dp[(idx,cur_sum)]

        if idx==len(nums):
            return 1 if cur_sum==target else 0
            
        # return backtrack(idx+1,cur_sum+nums[idx])+backtrack(idx+1,cur_sum-nums[idx])
        dp[(idx,cur_sum)]=(backtrack(idx+1,cur_sum+nums[idx]) +
                           backtrack(idx+1,cur_sum-nums[idx]))
        
        return dp[(idx,cur_sum)]
    
    return backtrack(0,0)

def targetSum(nums,target):
    # using bottom up approach
    # create 2d array dp[idx][cur_sum] to store ways to reach cur_sum at idx
    dp=[defaultdict(int) for _ in range(len(nums)+1)]

    dp[0][0]=1 # 0 elements 0 sum -> 1 way

    for i in range(len(nums)):
        for cur_sum,count in dp[i].items():
            dp[i+1][cur_sum+nums[i]]+=count
            dp[i+1][cur_sum-nums[i]]+=count

    return dp[len(nums)][target]

def spaceOptimization(nums,target):
    dp=defaultdict(int)

    dp[0]=1 # 0 sum -> 1 way

    for i in range(len(nums)):
        next_dp=defaultdict(int)
        for cur_sum,count in dp.items():
            next_dp[cur_sum+nums[i]]+=count
            next_dp[cur_sum-nums[i]]+=count
        # update dp
        dp=next_dp

    return dp[target]

arr=[1,1,1,1,1]
target=3
print(findTargetSumWays(arr,target))
print(targetSum(arr,target))
print(spaceOptimization(arr,target))