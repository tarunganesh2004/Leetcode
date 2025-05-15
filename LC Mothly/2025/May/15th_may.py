# Longest Unequal Adjacent Groups Subsequence I LC 2900

words=["e","a","b"]
groups=[0,0,1]

def getLngestSubsequence(words,groups):
    n=len(groups)
    cur_group=-1
    res=[]

    if n==1:
        return words 
    
    for i in range(n):
        if groups[i]!=cur_group:
            cur_group=groups[i]
            res.append(words[i])
    
    return res

print(getLngestSubsequence(words,groups))