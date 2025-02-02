# Longest Subarray of 1's After Deleting One Element LC 1493

# Given an array of integers, return the maximum length of a subarray that contains only 1's after you've deleted one element from the array.

nums=[1,1,0,1]

# brute force
def longestSubarrayBrute(nums):
    # brute force, iterate through the array and check if the subarray is valid
    # if it is valid, check if it is the longest
    # if it is the longest, update the longest
    def isValid(arr):
        return arr.count(0)<=1
    
    longest=0
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if isValid(nums[i:j+1]):
                longest=max(longest,j-i)
    return longest

# sliding window
def longestSubarray(nums):
    n=len(nums)
    res=0
    left=0
    right=0
    zeroCount=0
    while right<n:
        if nums[right]==0:
            zeroCount+=1
        while zeroCount>1:
            if nums[left]==0:
                zeroCount-=1
            left+=1
        res=max(res,right-left)
        right+=1

    return res

print(longestSubarrayBrute(nums))
print(longestSubarray(nums))