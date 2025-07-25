# Maximum Unique Subarray Sum After Deletion LC 3487

nums= [1, 2, 3, 4, 5]

def maxSum(nums):
    ans=0
    for num in set(nums):
        if num>0:
            ans+=num

    return ans if ans else max(nums)

print(maxSum(nums))  # Output: 15