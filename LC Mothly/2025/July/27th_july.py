# Count Hills and Valleys in an Array LC 2210

nums=[2,4,1,1,6,5]

def countHillsAndValleys(nums):
    n=len(nums)
    res=0
    for i in range(1, n-1):
        if nums[i]==nums[i+1]:
            nums[i]=nums[i-1]
        elif nums[i-1]>nums[i]<nums[i+1] or nums[i-1]<nums[i]>nums[i+1]:
            res+=1
    return res

print(countHillsAndValleys(nums))  # Output: 3