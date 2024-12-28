# Permutations II LC 47
# Given a collection of numbers that might contain duplicates, return all possible unique permutations.

def permuteUnique(nums):
    # approach is to use a map to keep track of the frequency of each number
    # then use backtracking to generate the permutations
    freq_map={}
    for num in nums:
        if num in freq_map:
            freq_map[num]+=1
        else:
            freq_map[num]=1
    res=[]

    def backtrack(path):
        if len(path)==len(nums):
            res.append(path)
            return

        for num in freq_map:
            if freq_map[num]>0:
                freq_map[num]-=1
                backtrack(path+[num])
                freq_map[num]+=1 # increase the frequency of the number back to the original value

    backtrack([])
    return res


nums=[1,1,2]
print(permuteUnique(nums)) 