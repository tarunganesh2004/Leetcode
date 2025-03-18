# # Longest Nice Subarray LC 2401
# You are given an array nums consisting of positive integers.

# We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.

# Return the length of the longest nice subarray.

# A subarray is a contiguous part of an array.

# Note that subarrays of length 1 are always considered nice.

 

nums=[1,3,8,48,10]

def longestNiceBruteForce(nums):
    n=len(nums)
    for i in range(n,0,-1):
        for j in range(n-i+1):
            sub=nums[j:j+i]
            print(sub)
            if all(sub[k]&sub[l]==0 for k in range(len(sub)) for l in range(k+1,len(sub))):
                return i
    return 0

# sliding window approach
def longestNiceSubarray(nums):
    used=0
    j=0
    res=0
    for i in range(len(nums)):
        while((used&nums[i])!=0):
            used^=nums[j]
            j+=1
        used|=nums[i]
        res=max(res,i-j+1)
    return res


print(longestNiceBruteForce(nums))
print(longestNiceSubarray(nums))