# Count subarrays of length 3 with a condition LC 3392

nums=[1,2,1,4,1]

def countSubarrays(nums):
    n=len(nums)
    res=0
    for i in range(1,n-1):
        if nums[i]==(nums[i-1]+nums[i+1])*2:
            res+=1
    return res

print(countSubarrays(nums)) # Output: 1