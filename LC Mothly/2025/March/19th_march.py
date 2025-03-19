# Minimum Operations to Make Binary Array Elements Equal to One LC 3191

nums=[0,1,1,1,0,0]

def minOperations(nums):
    count=0
    for i in range(2,len(nums)):
        if nums[i-2]==0:
            count+=1
            # flip i-2,i-1,i
            nums[i-2]=nums[i-2]^1
            nums[i-1]=nums[i-1]^1
            nums[i]=nums[i]^1

    if sum(nums)==len(nums):
        return count
    return -1

print(minOperations(nums))