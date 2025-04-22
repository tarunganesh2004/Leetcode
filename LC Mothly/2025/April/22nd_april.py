# Count the Number of Ideal Arrays LC 2338 Hard

from math import comb
from typing import Counter


n=2
maxValue=5

def idealArrays(n,maxValue):
    mod=10**9+7
    ans=maxValue
    freq={x:1 for x in range(1,maxValue+1)}
    for k in range(1,n):
        temp=Counter()
        for x in freq:
            for m in range(2,maxValue//x+1):
                ans+=comb(n-1,k)*freq[x]
                temp[x*m]+=freq[x]
        freq=temp
        ans=ans%mod
    return ans

print(idealArrays(n,maxValue)) # Output: 10