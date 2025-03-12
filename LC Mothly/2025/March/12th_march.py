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