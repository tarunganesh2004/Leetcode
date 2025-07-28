# Count Number of Maximum Bitwise OR Subsets LC 2044

from collections import Counter
nums=[3,1]

def countMaxOrSubsets(nums):
    pool=Counter()
    for cur in nums:
        pool[0]=1
        for prev,times in [*pool.items()]:
            pool[prev|cur]+=times

    return pool.most_common(1)[0][1]

print(countMaxOrSubsets(nums))  # Output: 2