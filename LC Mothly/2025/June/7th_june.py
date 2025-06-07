# Lexicographically Minimum String After Removing Stars

s="aaba*"
def clearStars(s):
    n=len(s)
    buckets=[[] for _ in range(26)]
    removed=[False]*n
    for i in range(n):
        if s[i]=="*":
            removed[i]=True
            for j in range(26):
                if buckets[j]:
                    removed[buckets[j].pop()]=True
                    break
        else:
            buckets[ord(s[i])-ord('a')].append(i)
    res=[]
    for i in range(n):
        if not removed[i]:
            res.append(s[i])
    return ''.join(res)


print(clearStars(s))  