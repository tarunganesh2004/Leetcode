# Count of Substrings Containing Every Vowel and K Consonants II LC 3306

from collections import defaultdict


s="aeioqq"
k=1

def bruteForce(s,k): # TLE
    n=len(s)
    def solve(str,k):
        v="aeiou"
        arr=[0]*5
        cons=0
        for ch in str:
            for i in range(5):
                if v[i]==ch:
                    arr[i]+=1
        
        for ch in str:
            if ch not in v:
                cons+=1

        all_v=(sum(arr)==5)
        all_c=(cons==k)
        return all_v and all_c
    res=0
    for i in range(n):
        for j in range(i,n):
            str=s[i:j+1]
            if solve(str,k):
                res+=1
    return res

# optimized solution is to use sliding window
def countOfSubstrings(s,k):
    def atleast(k):
        v=defaultdict(int)
        non_vowel=0
        res=0
        left=0
        for right in range(len(s)):
            if s[right] in "aeiou":
                v[s[right]]+=1
            else:
                non_vowel+=1
            while len(v)==5 and non_vowel>=k:
                res+=(len(s)-right)
                if s[left] in "aeiou":
                    v[s[left]]-=1
                else:
                    non_vowel-=1
                if v[s[left]]==0:
                    v.pop(s[left])
                left+=1
        return res 
    
    return atleast(k)-atleast(k+1)

print(bruteForce(s,k))
print(countOfSubstrings(s,k))