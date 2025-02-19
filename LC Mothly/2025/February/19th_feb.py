# # The k-th Lexicographical String of All Happy Strings of Length n LC 1415

# A happy string is a string that:

# consists only of letters of the set ['a', 'b', 'c'].
# s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
# For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

# Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

# Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

n=1
k=3
# [a,b,c], 3rd string is c

# approach is to generate all happy strings of length n and return the kth string
# using backtracking

def getHappyString(n,k):
    def backtrack(cur_str):
        if len(cur_str)==n:
            res.append(cur_str)
            return
        for c in ['a','b','c']:
            if not cur_str or cur_str[-1]!=c:
                backtrack(cur_str+c)
    res=[]
    backtrack("")
    return res[k-1] if k<=len(res) else ""

print(getHappyString(n,k))