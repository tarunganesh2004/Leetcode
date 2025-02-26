# Maximum Absolute Sum of Any Subarray LC 1749

arr=[1,-3,2,3,-4]

# brute force approach
def maxAbsoluteSumBrute(arr):
    res=0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            res=max(res,abs(sum(arr[i:j+1])))
    return res

# optimized approach is to keep track of max and min sum till i
def maxAbsoluteSum(arr):
    prefix_sum=0
    max_sum=0
    min_sum=0

    for num in arr:
        prefix_sum+=num
        max_sum=max(max_sum,prefix_sum)
        min_sum=min(min_sum,prefix_sum)

    return max_sum-min_sum

print(maxAbsoluteSumBrute(arr)) # 5