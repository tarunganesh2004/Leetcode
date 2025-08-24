# Longest Subarray of 1's After Deleting One Element LC 1493

nums=[1,1,0,1]

def longestSubarray(nums):
    n=len(nums)
    res=0
    left=0
    zeroCount=0
    for right in range(n):
        if nums[right]==0:
            zeroCount+=1
        
        while zeroCount>1:
            if nums[left]==0:
                zeroCount-=1
            left+=1
        res=max(res,right-left)

    return res

print(longestSubarray(nums))