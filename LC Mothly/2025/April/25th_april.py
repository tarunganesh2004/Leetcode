# # Count of Interesting Subarrays LC 2845
# You are given a 0-indexed integer array nums, an integer modulo, and an integer k.

# Your task is to find the count of subarrays that are interesting.

# A subarray nums[l..r] is interesting if the following condition holds:

# Let cnt be the number of indices i in the range [l, r] such that nums[i] % modulo == k. Then, cnt % modulo == k.

from collections import defaultdict


nums=[3,2,4]
modulo=2
k=1

# brute force
def bruteForce(nums,modulo,k):
    count=0
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            cnt=0
            for m in range(i,j+1):
                if nums[m]%modulo==k:
                    cnt+=1
            if cnt%modulo==k:
                count+=1
    return count

# the optimized approach is to use prefix sums
def optimized(nums,modulo,k):
    count=0
    prefix=0
    freq=defaultdict(int)
    freq[0]=1
    for num in nums:
        if num%modulo==k:
            prefix+=1 # treat as 1
        # now we need (prefix-prev_prefix)%modulo==k
        key=(prefix-k)%modulo
        count+=freq[key]
        # update the frequency map
        freq[prefix%modulo]+=1
    return count

print(bruteForce(nums,modulo,k)) # Output: 3
print(optimized(nums,modulo,k)) # Output: 3