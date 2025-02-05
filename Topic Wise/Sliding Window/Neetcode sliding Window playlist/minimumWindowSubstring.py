# Minimum Window Substring LC 76

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

s="ADOBECODEBANC"
t="ABC"
# o/p: "BANC" , in BANC all the characters of t are present

# brute force approach is to generate all the substrings of s and check if it contains all the characters of t
# but it takes more time
def bruteForce(s,t):
    n=len(s)
    ans=""
    def containsAll(s,t):
        for char in t:
            if char not in s:
                return False
        return True
    for i in range(n):
        for j in range(i+1,n+1):
            if containsAll(s[i:j],t):
                if ans=="" or len(ans)>len(s[i:j]):
                    ans=s[i:j]
    return ans

# sliding window approach
# using two maps one for what we have(s) and one for what we need(t)
def slidingWindow(s,t):
    if t=="" or s=="":
        return ""
    countT,window={},{} # countT stores the count of characters in t and window stores the count of characters in the window

    for char in t:
        countT[char]=countT.get(char,0)+1
    
    have=0
    need=len(countT)
    res=[-1,-1]
    resLen=float('inf') # res stores the start and end index of the substring
    left=0

    for right in range(len(s)):
        c=s[right]
        window[c]=window.get(c,0)+1

        if c in countT and window[c]==countT[c]:
            have+=1

        while have==need:
            # update the result
            if (right-left+1)<resLen:
                res=[left,right]
                resLen=right-left+1

            # pop from the left of the window
            window[s[left]]-=1
            if s[left] in countT and window[s[left]]<countT[s[left]]:
                have-=1
            left+=1
    i,j=res
    return s[i:j+1] if resLen!=float('inf') else ""

print(bruteForce(s,t)) # BANC
print(slidingWindow(s,t)) # BANC