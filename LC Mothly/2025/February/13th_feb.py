# # Minimum Operations to Exceed Threshold Value II LC 3066

# You are given a 0-indexed integer array nums, and an integer k.

# In one operation, you will:

# Take the two smallest integers x and y in nums.
# Remove x and y from nums.
# Add min(x, y) * 2 + max(x, y) anywhere in the array.
# Note that you can only apply the described operation if nums contains at least two elements.

# Return the minimum number of operations needed so that all elements of the array are greater than or equal to k.

import heapq

nums=[2,11,10,1,3]
k=10

# Brute Force O(n^2)
def minOperationsBrute(nums,k):
    operations=0
    while min(nums)<k:
        nums.sort()
        if len(nums)==1:
            return -1
        operations+=1
        x,y=nums[0],nums[1]
        nums.pop(0)
        nums.pop(0)
        nums.append(min(x,y)*2+max(x,y))
    return operations

# Using Priority Queue O(nlogn)
def minOperations(nums,k):
    h=[]
    for n in nums:
        heapq.heappush(h,n)
    operations=0
    while h[0]<k:
        if len(h)==1:
            return -1
        operations+=1
        x=heapq.heappop(h)
        y=heapq.heappop(h)
        heapq.heappush(h,min(x,y)*2+max(x,y))
    return operations

# print(minOperationsBrute(nums,k))
print(minOperations(nums,k))