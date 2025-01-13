# # Minimum Length of String After Operations LC 3223

# You are given a string s.

# You can perform the following process on s any number of times:

# Choose an index i in the string such that there is at least one character to the left of index i that is equal to s[i], and at least one character to the right that is also equal to s[i].
# Delete the closest character to the left of index i that is equal to s[i].
# Delete the closest character to the right of index i that is equal to s[i].
# Return the minimum length of the final string s that you can achieve

from collections import Counter
s="abaacbcbb" # select a at index 2 and delete a at index 0 and at index 3
# s="bacbcbb" # select b at index 3 and delete b at index 5 and at index 0
# s=acbcb so min length=5

def minimumLength(s): # O(n) & O(n)
    if len(s)<=2:
        return len(s)
    # approach is to use a map,
    # if a character frequency is odd then we should delete all characters except one
    # if a character frequency is even then we should delete all characters except two
    freq=Counter(s)

    delete_count=0
    for f in freq.values():
        if f%2==1:
            delete_count+=f-1 # delete all except one
        else:
            delete_count+=f-2 # delete all except two
    
    return len(s)-delete_count

# using constant space O(26),using freq array 
def minLen(s):
    chr_freq=[0]*26
    total_len=0

    for c in s:
        chr_freq[ord(c)-ord('a')]+=1

    for f in chr_freq:
        if f==0:
            continue # skip characters that dont appear
        if f%2==0:
            total_len+=2
        else:
            total_len+=1

    return total_len

print(minimumLength(s)) # 5
print(minLen(s)) # 5