# Shortest Common Supersequence LC 1092

# Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If multiple answers exist, you may return any of them.

# (A string S is a subsequence of string T if deleting some number of characters from T (possibly 0, and the characters are chosen anywhere from T) results in the string S.)

s1="abac"
s2="cab"

# brute force approach
# find all subsequences of s1 and s2
# find the common subsequence
def shortestCommonSupersequenceBrute(s1,s2): # TLE
    if not s1 and not s2:
        return ""
    # backtracking
    if not s1:
        return s2
    if not s2:
        return s1
    
    if s1[0]==s2[0]:
        return s1[0]+shortestCommonSupersequenceBrute(s1[1:],s2[1:])
    else:
        p1=s1[0]+shortestCommonSupersequenceBrute(s1[1:],s2)
        p2=s2[0]+shortestCommonSupersequenceBrute(s1,s2[1:])
    return p1 if len(p1)<len(p2) else p2
    
# optimized approach
# dp[i][j] will store the shortest common supersequence of s1[:i] and s2[:j]
# if s1[i]==s2[j] then dp[i][j]=1+dp[i-1][j-1]
# else dp[i][j]=1+min(dp[i-1][j],dp[i][j-1])
# idea is to use lcs to find the common subsequence

def shortestCommonSupersequence(s1,s2):
    if s1==s2:
        return s1
    n,m=len(s1),len(s2)
    dp=[[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    i,j=n,m
    res=""
    while i>0 and j>0:
        if s1[i-1]==s2[j-1]:
            res+=s1[i-1]
            i-=1
            j-=1
        else:
            if dp[i-1][j]>dp[i][j-1]:
                res+=s1[i-1]
                i-=1
            else:
                res+=s2[j-1]
                j-=1
    while i>0:
        res+=s1[i-1]
        i-=1
    while j>0:
        res+=s2[j-1]
        j-=1
    return res[::-1]

print(shortestCommonSupersequence(s1,s2)) # "cabac"