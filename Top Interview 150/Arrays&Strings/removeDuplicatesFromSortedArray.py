# Remove duplicates from sorted array LC 26

nums=[1,1,2]

# using set
def removeDuplicatesUsingSet(nums):
    nums[:]=sorted(set(nums))
    return len(nums)

# using two pointers
def removeDuplicates(nums):
    j=1
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]:
            nums[j]=nums[i]
            j+=1
    return j

print(removeDuplicatesUsingSet(nums))
print(removeDuplicates(nums))