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

print(bruteForce(s))