# Number of Subsequences That Satisfy the Given Sum Condition LC 1498

nums=[3,5,6,7]
target=9

def numSubseq(nums, target):
    nums.sort()
    left, right = 0, len(nums) - 1
    count = 0
    mod = 10**9 + 7
    
    while left <= right:
        if nums[left] + nums[right] <= target:
            count += pow(2, right - left, mod)
            left += 1
        else:
            right -= 1
            
    return count % mod

print(numSubseq(nums, target))  # Output: 4