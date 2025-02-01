# # Special Array I 

# An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

# You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.

nums=[2,1,4]

def isArraySpecial(nums):
    if len(nums)<2:
        return True
    for i in range(len(nums)-1):
        if (nums[i]%2==0 and nums[i+1]%2==0) or (nums[i]%2!=0 and nums[i+1]%2!=0):
            return False
    return True

print(isArraySpecial(nums))