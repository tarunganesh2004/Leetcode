# Type of Triangle LC 3024

nums=[3,3,3]

def triangleType(nums):
    def isEquilateral(nums):
        return nums[0] == nums[1] == nums[2]
    def isIsosceles(nums):
        # condition 1
        c1= nums[0] == nums[1] or nums[0] == nums[2] or nums[1] == nums[2]
        # condition 2
        c2= nums[0]+nums[1]>nums[2] and nums[0]+nums[2]>nums[1] and nums[1]+nums[2]>nums[0]
        return c1 and c2
    
    def isScalene(nums):
        return nums[0]+nums[1]>nums[2] and nums[0]+nums[2]>nums[1] and nums[1]+nums[2]>nums[0]
    
    if isEquilateral(nums):
        return "equilateral"
    elif isIsosceles(nums):
        return "isosceles"
    elif isScalene(nums):
        return "scalene"
    else:
        return "none"
    
print(triangleType(nums))  # Output: "equilateral"