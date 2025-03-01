# Apply operations to an array LC 2460

nums=[1,2,2,1,1,0]

def applyOperations(nums):
    for i in range(len(nums)-1):
        if nums[i]==nums[i+1]:
            nums[i]*=2
            nums[i+1]=0
        else:
            continue

    # move zeroes to end
    l,r=0,0  # noqa: E741
    while r<len(nums):
        if nums[r]!=0:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1  # noqa: E741
        r+=1
    return nums

print(applyOperations(nums))