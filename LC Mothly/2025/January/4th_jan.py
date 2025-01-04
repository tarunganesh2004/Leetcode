# Unique Length-3 Palindromic Subsequences LC 1930

s="aabca" # 3, i.e aba,aca, aaa

def bruteForce(s): # O(n^3) time and O(n) space
    n=len(s)
    unique_palindromes=set()

    # Generate all substrings of length 3
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                # form the subsequence
                subsequence=s[i]+s[j]+s[k]
                # check if it is a palindrome
                if subsequence==subsequence[::-1]:
                    unique_palindromes.add(subsequence)
    return len(unique_palindromes)

def countPalindromicSubsequences(s):
    # precompute first and last indices
    first,last=[-1]*26,[-1]*26
    for i in range(len(s)):
        cur=ord(s[i])-ord('a')
        if first[cur]==-1:
            first[cur]=i
        last[cur]=i

    ans=0
    for i in range(26):
        if first[i]==-1:
            continue

        between=set()
        for j in range(first[i]+1,last[i]):
            between.add(s[j])

        ans+=len(between)
    return ans
    

print(bruteForce(s))
print(countPalindromicSubsequences(s))