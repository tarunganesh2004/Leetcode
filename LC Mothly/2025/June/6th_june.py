# Using a Robot to Print the Lexicographically Smallest String LC 2434

from collections import Counter


s="zza"

def robotWithString(s):
    cnt=Counter(s)
    stack=[]
    res=[]
    minChar="a"
    for c in s:
        stack.append(c)
        cnt[c]-=1
        while minChar!= "z" and cnt[minChar] == 0:
            minChar=chr(ord(minChar)+1)
        while stack and stack[-1] <= minChar:
            res.append(stack.pop())
    
    return ''.join(res)

print(robotWithString(s))  # Output: "azz"