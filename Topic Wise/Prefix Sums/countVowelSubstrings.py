# Count Vowel Strings in Ranges LC 2559

words=["aba","bcb","ece","aa","e"]
queries=[[0,2],[1,4],[1,1]]

# Brute Force O(n*m) where n is the length of words and m is the length of queries

def vowelSubstringsBrute(words,queries): # 92/93 passed, tle
    def isVowel(s):
        return s in "aeiou"
    
    res=[]
    for li,ri in queries:
        count=0
        for i in range(li,ri+1):
            if isVowel(words[i][0]) and isVowel(words[i][-1]):
                count+=1
        res.append(count)
    return res

# Optimized O(n+m) where the approach is to use prefix sums
def vowelSubstrings(words,queries):
    def isVowel(s):
        return s in "aeiou"
    
    # Use a boolean array to mark vowel words
    vowel_flags=[isVowel(w[0]) and isVowel(w[-1]) for w in words]

    # Now build the prefix sum array storing the count of vowel words till the previous index
    prefix_sum=[0]*len(vowel_flags)

    prefix_sum[0]=1 if vowel_flags[0] else 0 # starting word if it is vowel then 1 else 0
    for i in range(1,len(vowel_flags)):
        prefix_sum[i]=prefix_sum[i-1]+(1 if vowel_flags[i] else 0) # For words ["aba","bcb","ece","aa","e"] prefix_sum=[1,1,2,3,4]

    res=[]
    for li,ri in queries: #[[0,2],[1,4],[1,1]]
        # prefix sum [1,1,2,3,4]
        # print(res)
        # print(li,ri)
        if li==0:
            res.append(prefix_sum[ri])
        else:
            # in range [li,ri] if asked to find the count then we can use ending- starting+1, i.e prefix_sum[ri]-prefix_sum[li-1]
            res.append(prefix_sum[ri]-prefix_sum[li-1])
    return res

print(vowelSubstringsBrute(words,queries))

print(vowelSubstrings(words,queries))