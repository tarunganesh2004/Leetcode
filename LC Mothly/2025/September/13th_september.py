# Find Most Frequent Vowel and Consonant LC 3541

s="succcesses"

def maxFreqSum(s):
    from collections import Counter
    vowels = 'aeiou'
    s=Counter(s)
    c1,c2=0,0
    for k,v in s.items():
        if k in vowels:
            c1=max(c1,v)
        else:
            c2=max(c2,v)
    return c1+c2

print(maxFreqSum(s))