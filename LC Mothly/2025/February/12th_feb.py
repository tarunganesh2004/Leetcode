# # Max Sum of a Pair Equal to sum of digits LC 2342

# You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

# Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

import heapq


nums=[18,43,36,13,7]

# Brute Force O(n^2)
def maximumSumBrute(nums):
    max_sum=-1
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if sum([int(x) for x in str(nums[i])])==sum([int(x) for x in str(nums[j])]):
                max_sum=max(max_sum,nums[i]+nums[j])
    return max_sum

# using sorting O(nlogn)
def maximumSumUsingSorting(nums):
    digit_sum_pairs=[]
    def calculate(num):
        s=0
        while num>0:
            s+=num%10
            num//=10
        return s
    for num in nums:
        d=calculate(num)
        digit_sum_pairs.append((d,num))
    digit_sum_pairs.sort()
    max_sum=-1
    for idx in range(1,len(digit_sum_pairs)):
        cur=digit_sum_pairs[idx][0]
        prev=digit_sum_pairs[idx-1][0]
        if cur==prev:
            cur=(digit_sum_pairs[idx][1]+digit_sum_pairs[idx-1][1])
            max_sum=max(max_sum,cur)
    return max_sum

# using priority Queue O(nlogm) where m is the maximum number of digits in a number
def usingPriorityQueue(nums):
    d_groups=[[] for _ in range(82)] #( 0 to 81)
    max_sum=-1
    def cal(num):
        s=0
        while num>0:
            s+=num%10
            num//=10
        return s
    
    for n in nums:
        d=cal(n)
        heapq.heappush(d_groups[d],n)

        if len(d_groups[d])>2:
            heapq.heappop(d_groups[d])

    for d_group in d_groups:
        if len(d_group)==2:
            first=heapq.heappop(d_group)
            second=heapq.heappop(d_group)
            max_sum=max(max_sum,first+second)
    return max_sum

# other way using dictionary
def optimized(nums):
    d,mx=dict(),-1
    for num in nums:
        sm,n=0,num
        while n>0:
            sm+=n%10
            n//=10
        if sm in d:
            if d[sm][0]<=num:
                d[sm][1]=d[sm][0]
                d[sm][0]=num
            elif d[sm][1]<num:
                d[sm][1]=num
        else:
            d[sm]=[num,-1]
    for key in d:
        if d[key][1]!=-1:
            mx=max(mx,d[key][0]+d[key][1])
    return mx

print(maximumSumBrute(nums)) # 54
print(maximumSumUsingSorting(nums)) # 54
print(usingPriorityQueue(nums)) # 54
print(optimized(nums)) # 54