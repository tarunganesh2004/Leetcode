# Subsets LC 78

nums=[1,2,3]

def subsets(nums): # TC O(2^n) SC O(2^n)
    res=[]
    def backtrack(start,path):
        res.append(path)
        for i in range(start,len(nums)):
            backtrack(i+1,path+[nums[i]])
    backtrack(0,[])
    return res

def anotherApproach(nums):
    res=[]

    subset=[]
    def generate(i):
        if i>=len(nums):
            res.append(subset.copy())
            return
        
        # include
        subset.append(nums[i])
        generate(i+1)

        # not include
        subset.pop()
        generate(i+1)
    
    generate(0)
    return res

print(subsets(nums))
print(anotherApproach(nums))