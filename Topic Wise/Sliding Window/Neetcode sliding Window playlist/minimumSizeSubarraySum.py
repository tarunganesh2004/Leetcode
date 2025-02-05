# Minimum Size Subarray Sum LC 209

# Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

nums=[2,3,1,2,4,3]
target=7 # we need to return minimum window of subarray whose sum is greater than or equal to target

# brute force approach is to generate all the subarrays and check if the sum is greater than or equal to target
# but it takes more time

def bruteForce(nums,target):
    n=len(nums)
    ans=float('inf')
    for i in range(n):
        for j in range(i+1,n+1):
            if sum(nums[i:j])>=target:
                ans=min(ans,j-i)
    return ans if ans!=float('inf') else 0

# sliding window approach
# we use two pointers left and right
def slidingWindow(nums,target):
    n=len(nums)
    left=0
    right=0
    ans=float('inf')
    cur_sum=0

    while right<n:
        cur_sum+=nums[right]
        while cur_sum>=target:
            ans=min(ans,right-left+1)
            cur_sum-=nums[left]
            left+=1
        right+=1
    return ans if ans!=float('inf') else 0

print(bruteForce(nums,target)) # 2
print(slidingWindow(nums,target)) # 2