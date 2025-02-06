# Tuple With Same Product LC 1726

# Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

nums=[2,3,4,6]

def tupleSameProduct(nums): # O(n^2) & O(n)
    from collections import defaultdict
    n=len(nums)
    count=0
    d=defaultdict(int)
    # print(d)
    for i in range(n):
        for j in range(i+1,n):
            # print(nums[i],nums[j])
            count+=8*d[nums[i]*nums[j]] # here 8 is multiplied because we have 4! ways to arrange 4 numbers
            # print(count)
            # print(d)
            d[nums[i]*nums[j]]+=1
            # print(d)
    return count

print(tupleSameProduct(nums))