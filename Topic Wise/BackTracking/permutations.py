# LC 46 Permutations
# Given a collection of distinct integers, return all possible permutations.

nums=[1,2,3]

def permute(nums):
    res=[]

    def backtrack(path):
        if len(path)==len(nums):
            res.append(path)
            return
        
        for num in nums:
            if num not in path:
                backtrack(path+[num])
            
    backtrack([])
    return res

def anotherApproach(nums):
    res=[]

    # base case
    if len(nums)==1:
        return [nums[:]]
    
    for i in range(len(nums)):
        n=nums.pop() # remove the last element
        p=anotherApproach(nums)
        for pe in p:
            pe.append(n)
        
        res.extend(p)
        nums.append(n)
    
    return res

print(permute(nums))
print(anotherApproach(nums))