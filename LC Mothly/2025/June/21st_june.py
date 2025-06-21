# Minimum Deletions to Make String K Spexial LC 3085

from collections import defaultdict


s="aabcaba"
k=0

def minimumDeletions(word,k):
    cnt=defaultdict(int)
    for c in word:
        cnt[c]+=1
    n=len(word)
    for a in cnt.values():
        deleted=0
        for b in cnt.values():
            if a>b:
                deleted+=b
            elif b>a-k:
                deleted+=b-(a+k)
        n=min(n,deleted)
    return n

print(minimumDeletions(s,k))  