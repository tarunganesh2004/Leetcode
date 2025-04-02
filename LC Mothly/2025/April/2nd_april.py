# Maximum Value of an Ordered Triplet I LC 2873

nums=[12,6,1,2,7]

# brute force
def bruteForce(nums): # O(n^3)
    n=len(nums)
    res=0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                res=max(res,(nums[i]-nums[j])*nums[k])
    return res

## Greedy
def maxTripletValue(nums):
    n=len(nums)
    res,imax,dmax=0,0,0
    for k in range(n):
        res=max(res,dmax*nums[k])
        dmax=max(dmax,imax-nums[k])
        imax=max(imax,nums[k])
    return res


print(bruteForce(nums))
print(maxTripletValue(nums))