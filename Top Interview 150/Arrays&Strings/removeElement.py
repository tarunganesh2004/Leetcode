# Remove Element LC 27

nums=[3,2,2,3]
val=3

def removeElement(nums,val):
    i=0
    for j in range(len(nums)):
        if nums[j]!=val:
            nums[i]=nums[j]
            i+=1
    return i

print(removeElement(nums,val))