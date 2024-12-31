# Make a subsequence using cyclic increments

def canMake(s1,s2):
    m=len(s1)
    n=len(s2)
    if n>m:
        return False
    
    first=0
    second=0
    while first<m and second<n:
        next= chr((ord(s1[first])-ord('a')+1)%26 + ord('a'))
        if s2[second]==s1[first] or s2[second]==next:
            second+=1
        first+=1

    return second==n

s1="abc"
s2="ad"
print(canMake(s1,s2))