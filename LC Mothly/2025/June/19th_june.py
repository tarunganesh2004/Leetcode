# Partition Array Such that Maximum Difference is K LC 2294

nums=[3,6,1,2,5]
k=2

def partitionArray(nums, k):
    nums.sort()
    ans=1
    start=nums[0]
    for i in range(1, len(nums)):
        if nums[i] - start > k:
            ans += 1
            start = nums[i]
    return ans

print(partitionArray(nums, k))  # Output: 2