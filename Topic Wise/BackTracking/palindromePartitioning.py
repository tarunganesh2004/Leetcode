# LC 131 Palindrome Partitioning

s="aab"

def palindromePartitioning(s):
    res=[]

    def isPalindrome(s):
        return s==s[::-1]
    
    def backtrack(start,path):
        if start==len(s):
            res.append(path)
            return
        
        for i in range(start,len(s)):
            if isPalindrome(s[start:i+1]):
                backtrack(i+1,path+[s[start:i+1]])
    
    backtrack(0,[])
    return res

def isPalin(s,i,j):
    while i<j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True
def anotherApproach(s):
    res=[]
    partitions=[]

    def dfs(i):
        if i>=len(s):
            res.append(partitions.copy())
            return
        
        for j in range(i,len(s)):
            if isPalin(s,i,j):
                partitions.append(s[i:j+1]) # pick
                dfs(j+1)
                partitions.pop() # backtrack
    dfs(0)
    return res

print(palindromePartitioning(s)) # [['a', 'a', 'b'], ['aa', 'b']]
print(anotherApproach(s)) # [['a', 'a', 'b'], ['aa', 'b']]