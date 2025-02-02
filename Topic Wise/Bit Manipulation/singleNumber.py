# Single Number LC 136
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

nums=[2,2,1]


def singleNumber(nums):
    # Using XOR operator
    a = 0
    for i in nums:
        a ^= i
    return a

print(singleNumber(nums))