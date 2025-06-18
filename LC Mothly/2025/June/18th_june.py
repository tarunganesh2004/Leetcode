# Divide Array into Arrays with Max Difference LC 2966

nums=[1,3,4,8,7,9,3,5,1]
k=2

def divideArray(nums, k):
    n=len(nums)
    if n%3!=0:
        return []
    nums.sort()

    result = []
    grp_idx=0
    for i in range(0, n, 3):
        if i+2<n and nums[i+2]-nums[i]<=k:
            result.append((nums[i], nums[i+1], nums[i+2]))
            grp_idx += 1
        else:
            return []
    return result

print(divideArray(nums, k))  