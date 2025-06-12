# Maximum Difference Between Adjacent Elements in a Circular Array LC 3423

nums=[1,2,4]

def maxAdjacentDistance(nums):
    n=len(nums)
    res=abs(nums[0]-nums[-1])
    for i in range(n-1):
        res=max(res,abs(nums[i]-nums[i+1]))
    return res

print(maxAdjacentDistance(nums))  # Output: 3