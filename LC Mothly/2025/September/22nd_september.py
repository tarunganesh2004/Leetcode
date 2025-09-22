# Count Elemts with Maximum Frequency LC 3005

from collections import Counter


nums=[1,2,2,3,1,4]

def maxFrequencyElement(nums):
    c=Counter(nums)
    max_freq=max(c.values())
    res=0
    for k,v in c.items():
        if v==max_freq:
            res+=v
    return res

print(maxFrequencyElement(nums))