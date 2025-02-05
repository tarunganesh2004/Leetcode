# Longest Substring without repeating characters LC 3

s="abcabcbb"

def bruteForce(s): # TLE 
    n=len(s)
    ans=0
    def isUnique(s,i,j):
        chars=set()
        for k in range(i,j):
            if s[k] in chars:
                return False
            chars.add(s[k])
        return True
    for i in range(n):
        for j in range(i+1,n+1):
            if isUnique(s,i,j):
                ans=max(ans,j-i)
    return ans

# using sliding window
def slidingWindow(s):
    n=len(s)
    seen=set()
    max_len=0
    left=0
    right=0
    while right<n:
        if s[right] not in seen:
            seen.add(s[right])
            right+=1
            max_len=max(max_len,right-left)
        else:
            seen.remove(s[left])
            left+=1
    return max_len

# other approach is to use hashmap to store the index of the character
def usingHashMap(s):
    map={}
    cur_len=0
    max_len=0
    for i,char in enumerate(s):
        if char not in map:
            cur_len+=1
        else:
            cur_len=min(i-map[char],cur_len+1)
        map[char]=i
        max_len=max(max_len,cur_len)
    return max_len

print(bruteForce(s)) # 3
print(slidingWindow(s)) # 3
print(usingHashMap(s)) # 3