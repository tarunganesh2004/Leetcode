# Sort Colors LC 75

nums=[2,0,2,1,1,0]

def sortColors(nums):
    c0=0
    c1=0
    c2=0
    for num in nums:
        if num==0:
            c0+=1
        elif num==1:
            c1+=1
        else:
            c2+=1
    i=0
    while c0>0:
        nums[i]=0
        i+=1
        c0-=1
    while c1>0:
        nums[i]=1
        i+=1
        c1-=1
    while c2>0:
        nums[i]=2
        i+=1
        c2-=1
    return nums

print(sortColors(nums))