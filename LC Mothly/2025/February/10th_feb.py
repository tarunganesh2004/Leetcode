# # Clear Digits LC 3174

# #You are given a string s.

# Your task is to remove all digits by doing this operation repeatedly:

# Delete the first digit and the closest non-digit character to its left.
# Return the resulting string after removing all digits.

s="cb34"

def clearDigits(s): # O(n) time and O(n) space
    stack=[]
    for i in s:
        if i.isdigit() and stack:
            stack.pop()
        else:
            stack.append(i)
    return "".join(stack)

# in place solution
def clearDigitsOptimized(s): # O(n) time and O(1) space
    res=0
    s=list(s)
    for chr_idx in range(len(s)):
        if s[chr_idx].isdigit():
            res=max(res-1,0)
        else:
            s[res]=s[chr_idx]
            res+=1
    return "".join(s[:res])

print(clearDigits(s)) 
print(clearDigitsOptimized(s))