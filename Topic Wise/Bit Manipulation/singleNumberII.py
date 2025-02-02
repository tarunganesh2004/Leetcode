# Single Number II LC 137
# Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

nums=[2,2,3,2]

# approach 1 using map(but not constant space)
def singleNumberUsingMap(nums):
    m={}
    for i in range(len(nums)):
        if nums[i] in m:
            m[nums[i]]+=1
        else:
            m[nums[i]]=1

    for key in m:
        if m[key]==1:
            return key
        
# approach 2 using bit manipulation
def singleNumber(nums):
    # two variables to keep track bits that appear once and twice
    ones=0
    twos=0
    for num in nums:
        # xor to track occurances of bits, and then remove bits that appear twice(~twos)
        ones=(ones^num)&~twos # keep track of bits that appear once
        twos=(twos^num)&~ones # moves bits to twos when they appear twice
    return ones # return the number that appears once
    
print(singleNumberUsingMap(nums))
print(singleNumber(nums))