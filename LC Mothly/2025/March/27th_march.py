# Minimum Index of a Valid Split LC 2780

nums=[1,2,2,2]

def minIndex(nums):
    from collections import defaultdict
    first_map=defaultdict(int)
    second_map=defaultdict(int)
    n=len(nums)
    for num in nums:
        second_map[num]+=1

    for idx in range(n):
        num=nums[idx]
        second_map[num]-=1
        first_map[num]+=1

        if(first_map[num]*2>idx+1 and second_map[num]*2>n-idx-1):
            return idx
    return -1

print(minIndex(nums))