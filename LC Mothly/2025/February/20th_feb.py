# Find Unique Binary String LC 1980

# Given an array of strings nums representing n binary strings, return a binary string that is not a binary string in nums. If there are multiple answers, you may return any of them

nums=["01","10"]
# 00 is not in nums

# approach is to generate all binary strings of length n and return the one that is not in nums
# using backtracking

def findDifferentBinaryString(nums):
    def backtrack(cur_str):
        if len(cur_str)==n:
            if cur_str not in nums:
                res.append(cur_str)
            return
        for c in ['0','1']:
            backtrack(cur_str+c)
    n=len(nums[0])
    res=[]
    backtrack("")
    return res[0]

# optimized approach , Cantor's diagonal argument
def optimized(nums):
    res=[]
    for i in range(len(nums)):
        cur=nums[i][i]
        if cur=='0':
            res.append('1')
        else:
            res.append('0')
    return "".join(res)


print(findDifferentBinaryString(nums))
print(optimized(nums))