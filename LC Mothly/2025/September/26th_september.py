# Valid Triangle Number LC 611

nums=[2,2,3,4]

def countTriangles(nums):
    nums.sort()
    count=0
    n=len(nums)
    for i in range(n-1,1,-1):
        left=0
        right=i-1
        while left<right:
            if nums[left]+nums[right]>nums[i]:
                count+=right-left
                right-=1
            else:
                left+=1
    return count

print(countTriangles(nums))