# Majority Element LC 169

nums=[3,2,3]

# using dictionary
def majorityElement(nums):
    d={}
    for i in nums:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for i in d:
        if d[i]>len(nums)//2:
            return i
        


# using O(1) space
def optimized(nums):
    count=0
    candidate=None
    for i in nums:
        if count==0:
            candidate=i
        count+=(1 if i==candidate else -1)
    return candidate

print(majorityElement(nums))
print(optimized(nums))