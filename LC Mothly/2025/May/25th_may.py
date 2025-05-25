# Longest Palindrome by Concatenationg two letter words LC 2131

from collections import defaultdict


words=["lc","cl","gg"]

def longestPalindrome(words):
    m=defaultdict(int)
    unpaired=ans=0
    for w in words:
        if w[0] == w[1]:
            if m[w] > 0:
                unpaired -= 1
                m[w]-= 1
                ans+=4
            else:
                m[w] += 1
                unpaired += 1
        else:
            if m[w[::-1]] > 0:
                ans += 4
                m[w[::-1]] -= 1
            else:
                m[w] += 1
    if unpaired > 0:
        ans += 2
    return ans


print(longestPalindrome(words))  # Output: 6