# Longest Subsequence Repeated K Times LC 2014

from collections import deque


s="letsleetcode"
k=2

def longestSubsequenceRepeatedK(s, k):
    def isK(sub,t,k):
        count=i=0
        for ch in t:
            if i<len(sub) and ch==sub[i]:
                i+=1
                if i==len(sub):
                    i=0
                    count+=1
                    if count==k:
                        return True
        return False
    
    res=""
    q=deque([""])
    while q:
        cur=q.popleft()
        for ch in map(chr,range(ord('a'),ord('z')+1)):
            next=cur+ch
            if isK(next,s,k):
                res=next
                q.append(next)
    return res

print(longestSubsequenceRepeatedK(s, k))  # Output: "let"