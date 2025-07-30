# Longest Subarray With Maximum Bitwise AND LC 2419

nums=[1,2,3,3,2,2]

def longestSubarray(nums):
    max_and = 0
    count=0
    max_count=0
    for i in range(len(nums)):
        max_and= max(max_and, nums[i])
    
    for i in range(len(nums)):
        if max_and==nums[i]:
            count+=1
        else:
            max_count=max(max_count, count)
            count=0
    max_count=max(max_count, count)
    if max_count==0:
        return 1
    return max_count

print(longestSubarray(nums))