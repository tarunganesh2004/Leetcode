# Count Complete Subarrays in an Array LC 2799

# We call a subarray of an array complete if the following condition is satisfied:

# The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.

nums=[1,3,1,2,2]

# brute force
def bruteForce(nums):
    # number of distinct elements in the whole array
    n=len(set(nums))
    count=0
    # generate each subarray
    for i in range(len(nums)):
        for j in range(i+1,len(nums)+1):
            # check if the subarray is complete
            if len(set(nums[i:j]))==n:
                count+=1
    return count

# optimized approach is to use sliding window

def countCompleteSubarrays(nums):
    k=len(set(nums))
    left=0
    res=0
    map={}
    for i in range(len(nums)):
        map[nums[i]]=map.get(nums[i],0)+1
        while len(map)==k:
            res+=len(nums)-i
            map[nums[left]]-=1
            if map[nums[left]]==0:
                del map[nums[left]]
            left+=1
    return res

print(bruteForce(nums)) # Output: 4
print(countCompleteSubarrays(nums)) # Output: 4