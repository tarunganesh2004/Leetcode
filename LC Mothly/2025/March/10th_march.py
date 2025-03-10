# Count of Substrings Containing Every Vowel and K Consonants II LC 3306

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

print(bruteForce(s,k))