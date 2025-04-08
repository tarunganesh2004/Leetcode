# Partition Equal Subset Sum LC 416

nums=[1,5,11,5]

# brute force
def brute_force(nums):
    # recursion
    def can_partition(i, sum1, sum2):
        if i == len(nums):
            return sum1 == sum2
        return can_partition(i + 1, sum1 + nums[i], sum2) or can_partition(i + 1, sum1, sum2 + nums[i])
    
    return can_partition(0, 0, 0)

# using lru_cache for memoization
from functools import lru_cache  # noqa: E402
def memoization(nums):
    @lru_cache(None)
    def can_partition(i, sum1, sum2):
        if i == len(nums):
            return sum1 == sum2
        return can_partition(i + 1, sum1 + nums[i], sum2) or can_partition(i + 1, sum1, sum2 + nums[i])
    
    return can_partition(0, 0, 0)

print(brute_force(nums))
print(memoization(nums))