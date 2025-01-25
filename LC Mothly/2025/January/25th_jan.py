# # Make Lexicographically smallest array by swapping elements LC 2948

# You are given a 0-indexed array of positive integers nums and a positive integer limit.

# In one operation, you can choose any two indices i and j and swap nums[i] and nums[j] if |nums[i] - nums[j]| <= limit.

# Return the lexicographically smallest array that can be obtained by performing the operation any number of times.

# An array a is lexicographically smaller than an array b if in the first position where a and b differ, array a has an element that is less than the corresponding element in b. For example, the array [2,10,3] is lexicographically smaller than the array [10,2,3] because they differ at index 0 and 2 < 10.

from collections import defaultdict
from heapq import heappush,heappop
nums=[1,5,3,9,8]
limit=2


def lexicographicallySmallestArray(nums,limit):
    unions=defaultdict(list)
    heads=defaultdict(int)
    head=prev=None
    for num in sorted(nums):
        if not head:
            head=prev=num
        elif abs(prev-num)<=limit:
            prev=num
        else:
            head=prev=num
        heads[num]=head
        heappush(unions[head],num)
    headList=[heads[n] for n in nums]
    return [heappop(unions[head]) for head in headList]

print(lexicographicallySmallestArray(nums,limit)) # [1,3,5,8,9]