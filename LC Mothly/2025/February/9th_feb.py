# # Count Number of Bad pairs LC 2364

# You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].

# Return the total number of bad pairs in nums.

from collections import defaultdict


nums=[4,1,3,3]

def bruteForce(nums):
    n=len(nums)
    count=0
    for i in range(n):
        for j in range(i+1,n):
            if i<j and j-i!=nums[j]-nums[i]:
                count+=1
    return count

def otherApproach(nums):
    good_pairs=0
    total_pairs=0
    count=defaultdict(int)
    for i in range(len(nums)):
        total_pairs+=i
        good_pairs+=count[i-nums[i]]
        count[i-nums[i]]+=1
    return total_pairs-good_pairs
    

def optimized(nums):
    n=len(nums)
    bad_pairs=0
    diff_count={}
    for i in range(n):
        diff=i-nums[i]
        good_pairs=diff_count.get(diff,0)
        bad_pairs+= (i-good_pairs)
        diff_count[diff]=good_pairs+1
    return bad_pairs

print(bruteForce(nums)) # 5
print(optimized(nums)) # 5