# Remove duplicates from sorted array II LC 80

nums=[1,1,1,2,2,3]

def removeDuplicates(nums):
    j=1
    count=1
    for i in range(1,len(nums)):
        if nums[i]==nums[i-1]:
            count+=1
        else:
            count=1
        if count<=2:
            nums[j]=nums[i]
            j+=1
    return j

# simple way
def remove(nums):
    i=2
    for j in range(2,len(nums)):
        if nums[j]>nums[i-2]:
            nums[i]=nums[j]
            i+=1
    return i

print(removeDuplicates(nums))