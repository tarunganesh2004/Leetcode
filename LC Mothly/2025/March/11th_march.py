# Number of Substrings Containing All Three Characters LC 1358

s="abcabc"

# brute force
def bruteForce(s): # TLE, O(n^3)
    n=len(s)
    res=0
    for i in range(n):
        for j in range(i,n):
            if len(set(s[i:j+1]))==3:
                res+=1
    return res

# optimized solution is to use sliding window
def optimized(s):
    n=len(s)
    res=0
    left=0
    cur_count={}
    for right in range(n):
        cur_count[s[right]]=cur_count.get(s[right],0)+1
        while len(cur_count)==3:
            res+=(n-right)
            cur_count[s[left]]-=1
            if cur_count[s[left]]==0:
                cur_count.pop(s[left])
            left+=1
    return res

print(bruteForce(s))
print(optimized(s))