# Count the Number of Fair Pairs LC 2563

nums=[0,1,7,4,4,5]
lower=3
upper=6

# brute force
def brute_force(nums,lower,upper):
    count=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if lower<=nums[i]+nums[j]<=upper:
                count+=1
    return count

# optimized approach 
def countFairPairs(nums,lower,upper):
    def countPairs(nums,target):
        count=0
        left,right=0,len(nums)-1
        while left<right:
            if nums[left]+nums[right]>target:
                right-=1
            else:
                count+=right-left
                left+=1
        return count
    
    nums.sort()
    return countPairs(nums,upper)-countPairs(nums,lower-1)

print(brute_force(nums,lower,upper)) # Output: 6

print(countFairPairs(nums,lower,upper)) # Output: 6