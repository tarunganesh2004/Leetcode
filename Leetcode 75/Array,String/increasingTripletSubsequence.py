# Increasing Triplet Subsequence

# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

nums=[1,2,3,4,5]

def increasingTriplet(nums):
    # approach is to keep track of the smallest and second smallest number
    # if we find a number greater than the second smallest number, we have found the triplet
    # if we find a number greater than the smallest number, we update the smallest number

    if len(nums) < 3:
        return False
    
    smallest = float('inf')
    second_smallest = float('inf')
    for num in nums:
        if num <= smallest:
            smallest = num
        elif num <= second_smallest:
            second_smallest = num
        else:
            return True
    return False

print(increasingTriplet(nums))