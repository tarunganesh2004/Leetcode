# Subsets II LC 90

nums=[1,2,2]

def subsetsII(nums):
    nums.sort()
    res=[]

    def backtrack(start,path):
        res.append(path)
        for i in range(start,len(nums)):
            if i>start and nums[i]==nums[i-1]:
                continue
            backtrack(i+1,path+[nums[i]])
    backtrack(0,[])
    return res

def anotherApproach(nums):
    res=[]
    subset=[]
    nums.sort()
    
    def dfs(i):
        if i>=len(nums):
            res.append(subset.copy())
            return
        
        # include
        subset.append(nums[i])
        dfs(i+1)

        # backtrack and not include
        subset.pop()

        # skip duplicates : only consider the next element if its different from the previous one
        while i+1<len(nums) and nums[i]==nums[i+1]:
            i+=1

        # not include
        dfs(i+1)

    dfs(0)
    return res

print(subsetsII(nums))
print(anotherApproach(nums))