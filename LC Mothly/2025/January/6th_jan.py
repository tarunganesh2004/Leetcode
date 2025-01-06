# Sum pair closest to target
# Given an array arr[] and a number target, find a pair of elements (a, b) in arr[], where a<=b whose sum is closest to target.
# Note: Return the pair in sorted order and if there are multiple such pairs return the pair with maximum absolute difference. If no such pair exists return an empty array.

arr=[10,30,20,5]
target=25

def closest_pair(arr,target):
    arr.sort()
    res=[arr[0],arr[-1]]
    left=0
    right=len(arr)-1
    while left<right:
        sum=arr[left]+arr[right]
        if abs(sum-target)<abs(sum-res[0]-res[1]):
            res=[arr[left],arr[right]]
        if sum>target:
            right-=1
        else:
            left+=1
    return res

def closest_pairAnother(arr,target):
    n=len(arr)
    if n<2:
        return []
    arr.sort()
    res=[]
    minDiff=float('inf')
    left=0
    right=n-1

    while left<right:
        curSum=arr[left]+arr[right]
        absDiff=abs(curSum-target)

        if absDiff<minDiff:
            res=[arr[left],arr[right]]
            minDiff=absDiff
        elif absDiff==minDiff:
            # if the current pair has the same difference as the previous pair, then we need to check if the current pair has a greater difference than the previous pair
            if abs(arr[right]-arr[left])>abs(res[1]-res[0]):
                res=[arr[left],arr[right]]
        if curSum>target:
            right-=1
        else:
            left+=1
    return res

print(closest_pair(arr,target))
print(closest_pairAnother(arr,target))