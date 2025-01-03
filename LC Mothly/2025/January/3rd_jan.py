# Number of ways to split array LC 2270

nums=[10,4,-8,7]

def waysTosplitArray(nums):
    prefix=[0]*len(nums)
    prefix[0]=nums[0]
    for i in range(1,len(nums)):
        prefix[i]=prefix[i-1]+nums[i]

    # print(prefix)
    total=prefix[-1]

    count=0
    for i in range(len(nums)-1):
        left=prefix[i]
        right=total-prefix[i]
        if left>=right:
            count+=1
    return count

def waysTosplitArrayOptimal(nums): # O(n) time and O(1) space
    left_sum=0
    right_sum=sum(nums)
    res=0
    for i in range(len(nums)-1):
        left_sum+=nums[i]
        right_sum-=nums[i]
        if left_sum>=right_sum:
            res+=1
    return res

print(waysTosplitArray(nums))
print(waysTosplitArrayOptimal(nums))