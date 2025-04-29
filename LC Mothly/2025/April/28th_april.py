# Count Subarrays with score less than K LC 2302(Hard)

nums=[2,1,4,3,5]
k=10

# brute Force O(n^3) solution
def countSubarrays(nums,k):
    n=len(nums)
    res=0
    for i in range(n):
        for j in range(i,n):
            sub=nums[i:j+1]
            if sum(sub)*len(sub)<k:
                res+=1
    return res

# using two pointers O(n^2) solution
def twoPointers(nums,k):
    count=0
    for right in range(len(nums)):
        sum=0
        for left in range(right,len(nums)):
            sum+=nums[left]
            if sum*(left-right+1)<k:
                count+=1
    return count

# optimized approach is to use sliding window O(n) solution
def optimized(nums,k):
    count=0
    sum=0
    left=0
    for right in range(len(nums)):
        sum+=nums[right]
        while sum*(right-left+1)>=k:
            sum-=nums[left]
            left+=1
        count+=right-left+1
    return count

print(countSubarrays(nums,k)) # Output: 6
print(twoPointers(nums,k)) 
print(optimized(nums,k)) # Output: 6