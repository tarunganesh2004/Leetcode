# Count Subarrays where max element appears atleast k times LC 2962

nums=[1,3,2,3,3]
k=2

# brute Force O(n^3) solution
def countSubarrays(nums,k):
    n=len(nums)
    res=0
    for i in range(n):
        for j in range(i,n):
            sub=nums[i:j+1]
            max_num=max(sub)
            if max_num in sub and sub.count(max_num)>=k:
                res+=1
    return res

# optimized using sliding window O(n) solution
def optimized(nums,k):
    max_ele=max(nums)
    count=0
    left=max_count=0
    for right in range(len(nums)):
        if nums[right]==max_ele:
            max_count+=1
        while max_count==k:
            count+=len(nums)-right
            if nums[left]==max_ele:
                max_count-=1
            left+=1
    return count

print(countSubarrays(nums,k)) # Output: 6

print(optimized(nums,k)) # Output: 6