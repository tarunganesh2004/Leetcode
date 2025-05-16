# Longest Unequal Adjacent Groups Subsequence II LC 2901

words=["bab","dab","cab"]
groups=[1,2,2]

def getLngestSubsequence(words,groups):
    def differbyOne(w1,w2):
        if len(w1)!=len(w2):
            return False
        
        diff=0
        for c1,c2 in zip(w1,w2):
            if c1!=c2:
                diff+=1
        return diff==1
    
    n=len(groups)
    dp=[1]*n
    parent=[-1]*n
    max_len=0
    for i in range(n):
        for j in range(i):
            if groups[i]!=groups[j] and differbyOne(words[i],words[j]) and dp[i]<dp[j]+1:
                dp[i]=dp[j]+1
                parent[i]=j
            
        if dp[i]>max_len:
            max_len=dp[i]
    
    res=[]
    for i in range(n):
        if dp[i]==max_len:
            while i!=-1:
                res.append(words[i])
                i=parent[i]
            break
    
    return res[::-1]

print(getLngestSubsequence(words,groups))