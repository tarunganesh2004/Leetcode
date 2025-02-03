# Longest Strictly Increasing or Strictly Decreasing Subarray LC 3105

nums=[1,4,3,3,2]

def longestMonoticSubarray(nums):
    n=len(nums)
    # check for Strictly Decreasing
    max_len=1
    tmp_count=1
    for i in range(1,n):
        if nums[i]>nums[i-1]:
            tmp_count+=1
            max_len=max(max_len,tmp_count)
        else:
            tmp_count=1
    # check for Strictly Increasing
    tmp_count=1
    for i in range(1,n):
        if nums[i]<nums[i-1]:
            tmp_count+=1
            max_len=max(max_len,tmp_count)
        else:
            tmp_count=1
    return max_len

print(longestMonoticSubarray(nums))