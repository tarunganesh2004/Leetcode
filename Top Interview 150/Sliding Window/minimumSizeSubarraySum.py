# Minimum Size subarray sum LC 209

nums=[2,3,1,2,4,3]
target=7

def minSubarrayLen(nums,target):
    n=len(nums)
    cur_sum=0
    res=float("inf")
    left=0
    for right in range(n):
        cur_sum+=nums[right]
        while cur_sum>=target:
            res=min(res,right-left+1)
            cur_sum-=nums[left]
            left+=1
    return res if res!=float("inf") else 0

print(minSubarrayLen(nums,target)) # 2