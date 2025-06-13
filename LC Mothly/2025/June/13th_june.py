# Minimize the Maximum Difference of Pairs LC 2616

nums=[10,1,2,7,1,3]
p=2

def minimizeMax(nums, p):
    nums.sort()
    n = len(nums)
    left,right= 0, nums[-1] - nums[0]
    while left<right:
        mid= (left + right) // 2
        k=0
        i=1
        while i < n:
            if nums[i] - nums[i - 1] <= mid:
                k += 1
                i += 1
            i += 1
        if k >= p:
            right = mid
        else:
            left = mid + 1
    return left

print(minimizeMax(nums, p))  # Output: 1