# Maximum Ascending Subarray Sum LC 1800

# Given an array of integers nums, return the maximum possible sum of an ascending subarray in nums.
# A subarray is defined as a contiguous sequence of numbers in an array.
# A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi < numsi+1.

# A subarray is strictly ascending if for all i where l <= i < r, numsi < numsi+1.

arr=[10,20,30,5,10,50]

def maxAscendingSum(arr):
    n=len(arr)
    max_sum=arr[0]
    tmp_sum=arr[0]
    for i in range(1,n):
        if arr[i]>arr[i-1]:
            tmp_sum+=arr[i]
            max_sum=max(max_sum,tmp_sum)
        else:
            tmp_sum=arr[i]
    return max_sum

print(maxAscendingSum(arr))