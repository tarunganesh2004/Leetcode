# Maximum Count of Positive and Negative Integers LC 2529

nums=[-2,-1,-1,1,2,3]

# general approach
def maxCount(nums):
    pos=0
    neg=0
    for i in nums:
        if i>0:
            pos+=1
        if i<0:
            neg+=1
    return max(pos,neg)

print(maxCount(nums))

# optimized approach is to use binary search
def optimized(nums):
    # return 1st index where value >=0
    def lower_bound(nums):
        start,end=0,len(nums)-1
        n=len(nums)
        while start<=end:
            mid=(start+end)//2
            if nums[mid]<0:
                start=mid+1
            else:
                end=mid-1
                n=mid
        return n
    
    # return 1st index where value >0
    def upper_bound(nums):
        start,end=0,len(nums)-1
        n=len(nums)
        while start<=end:
            mid=(start+end)//2
            if nums[mid]<=0:
                start=mid+1
            else:
                end=mid-1
                n=mid
        return n
    
    positive_count=len(nums)-upper_bound(nums)
    negative_count=lower_bound(nums)
    return max(positive_count,negative_count)

print(optimized(nums))