# Minimum Number of Operations to Make Elements in Array Distinct LC 3396

nums=[1,2,3,4,2,3,3,5,7]

# remove 3 elements from beginning or from end

def minOperations(nums):
    def checkUnique(start):
        seen=set()
        for num in nums[start:]:
            if num in seen:
                return False
            seen.add(num)
        return True
    
    res=0
    for i in range(0,len(nums),3):
        if checkUnique(i):
            return res
        res+=1
    return res

print(minOperations(nums))