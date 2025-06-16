# Maximum Difference Between Increasing Elements LC 2016

nums= [7, 1, 5, 4]

def maximumDifference(nums):
    max_diff = -1
    min_val = nums[0]

    for i in range(1, len(nums)):
        if nums[i] > min_val:
            max_diff = max(max_diff, nums[i] - min_val)
        else:
            min_val = nums[i]

    return max_diff

print(maximumDifference(nums))  # Output: 4