# Minimum Difference Sums After Removal of Elements LC 2163(Hard)

from collections import Counter
from heapq import heapify, heappop, heappush
nums=[3,1,2]

def minimumDifference(nums):
    n=len(nums)//3
    left=[-i for i in nums[:n]]
    heapify(left)
    right=sorted(nums[n:])[:n]
    first=sum(nums[:n])
    second=sum(nums[n:])-sum(right)
    taken=Counter()
    res=first-second
    for i in nums[n:-n]:
        if i< -left[0]:
            first=first+heappop(left)+i
            heappush(left, -i)
        if i>right[-1]:
            while taken[right[-1]]>0:
                taken[right[-1]]-=1
                right.pop()
            second=second+right[-1]-i
            right.pop()
        else:
            taken[i]+=1
        res=min(res, first-second)
    return res

print(minimumDifference(nums))  # Output: -1
