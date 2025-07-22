# Maximum Erasure Value LC 1695

nums=[4,2,4,5,6]

def maximumUniqueSubarray(nums):
    seen=set()
    left=0
    max_sum=0
    current_sum=0
    for right in range(len(nums)):
        while nums[right] in seen:
            seen.remove(nums[left])
            current_sum -= nums[left]
            left += 1
        seen.add(nums[right])
        current_sum += nums[right]
        max_sum = max(max_sum, current_sum)
    return max_sum

print(maximumUniqueSubarray(nums))  # Output: 17 