# Maximum Score after splitting a String LC 1422

s="011101"

# Brute Force
def maxScoreBrute(s):
    ans=0
    for i in range(len(s)-1):
        cur=0
        for j in range(i+1):
            if s[j]=='0':
                cur+=1
        for j in range(i+1,len(s)):
            if s[j]=='1':
                cur+=1
        ans=max(ans,cur)
    return ans

# Optimized
def maxScore(s):
    ones=s.count("1")
    zeros=0
    ans=0
    for i in range(len(s)-1):
        if s[i]=='1':
            ones-=1
        else:
            zeros+=1
        ans=max(ans,zeros+ones)

    return ans

print(maxScoreBrute(s))
print(maxScore(s))