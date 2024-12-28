# Permutations II LC 47
# Given a collection of numbers that might contain duplicates, return all possible unique permutations.

def permuteUnique(nums):
    res=[]
    s=set()

    def backtrack(path):
        if len(path)==len(nums):
            if tuple(path) not in s:
                res.append(path)
                s.add(tuple(path))
            return
        
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            if nums[i] not in path:
                backtrack(path+[nums[i]])
    nums.sort()
    backtrack([])
    return res

nums=[1,1,2]
print(permuteUnique(nums)) 