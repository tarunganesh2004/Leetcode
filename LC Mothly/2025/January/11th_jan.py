# Construct K palindrome Strings LC 1400

s="annabelle"
s1="leetcode"

def canConstruct(s,k):
    if len(s)<k:
        return False
    if len(s)==k:
        return True
    char_count=[0]*26

    for ch in s:
        char_count[ord(ch)-ord('a')]+=1
    odd_count=0
    for count in char_count:
        if count%2!=0:
            odd_count+=1
    return odd_count<=k

print(canConstruct(s,2)) # True
print(canConstruct(s1,3)) # False