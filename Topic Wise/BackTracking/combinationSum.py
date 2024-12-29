# Combination Sum LC 39

candidates=[2,3,6,7]
target=7

def combinationSum(candidates,target):
    res=[]

    def dfs(index,path,target):
        if target==0 or index==len(candidates):
            if target==0:
                res.append(path)
            return
        
        if target<0:
            return
        
        # include the current element
        dfs(index,path+[candidates[index]],target-candidates[index])

        # exclude the current element
        dfs(index+1,path,target)

    dfs(0,[],target)
    return res

def anotherApproach(candidates,target):
    res=[]

    def dfs(idx,cur,total):
        if total==target:
            res.append(cur.copy())
            return
        if total>target or idx>=len(candidates):
            return
        
        # include the current element
        cur.append(candidates[idx])
        dfs(idx,cur,total+candidates[idx])
        cur.pop()

        # exclude the current element
        dfs(idx+1,cur,total)

    dfs(0,[],0)
    return res

print(combinationSum(candidates,target)) # [[2, 2, 3], [7]]
print(anotherApproach(candidates,target)) # [[2, 2, 3], [7]]