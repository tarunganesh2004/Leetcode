# Remove All occurances of a substring LC 1910

# You are given two strings s and part. A string is called a superstring of another string if it contains that string as a substring.

# find the leftmost occurrence of part in s and remove it. Return the resulting string.

s="daabcbaabcbc"
part="abc"

def removeOccurrences(s,part): # O(n) time and O(n) space
    stack=[]
    for chr_idx in range(len(s)):
        stack.append(s[chr_idx])
        start=len(stack)-len(part)
        if len(stack)>=len(part) and "".join(stack[start:])==part:
            for _ in range(len(part)):
                stack.pop()
    return "".join(stack)

# using replace method O(1) space and O(n) time
def optimized(s,part):
    while part in s:
        s=s.replace(part,"",1) # 1 means only 1st occurance of part will be removed
    return s

print(removeOccurrences(s,part)) # "dab"
print(optimized(s,part)) # "dab"