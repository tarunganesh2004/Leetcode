# Frequency of the Most Frequent Element LC 1838

nums=[1,2,4]
k=5 # we are allowed to change at most k elements
# we can change 1 to 4 and 2 to 4, so the maximum frequency of any element is 3.

def maxFrequency(nums,k):
    nums.sort()
    l,r=0,0  # noqa: E741
    total=0
    res=0
    while r<len(nums):
        total+=nums[r]
        
        while nums[r]*(r-l+1) > total+k: #(r-l+1) is the window
            # shrink the window
            total-=nums[l]
            l+=1  # noqa: E741
        res=max(res,r-l+1)
        r+=1
    return res

def anotherApproach(nums,k):
    nums.sort()
    n=len(nums)
    ans=0
    i=0
    for j in range(n):
        k+=nums[j]
        while k<nums[j]*(j-i+1):
            k-=nums[i]
            i+=1
        ans=max(ans,j-i+1)
    return ans

print(maxFrequency(nums,k))
print(anotherApproach(nums,k))