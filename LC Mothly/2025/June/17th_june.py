# Count the Number of Arrays with K Matching Adjacent Elements LC 3405(Hard)

n=3
m=2
k=1

def countGoodArrays(n,m,k):
    from math import comb
    mod= 10**9 + 7
    return m*pow(m-1,n-k-1,mod)*comb(n-1,k)%mod

print(countGoodArrays(n, m, k))  # Output: 4