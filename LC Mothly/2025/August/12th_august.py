# Ways to Express an Integer as Sum of powers LC 2787

n=10
x=2

def numberOfWays(n,x):
    mod=10**9 + 7
    dp=[0]*(n+1)
    dp[0]=1

    for i in range(1,n+1):
        val=i**x 
        if val>n:
            break
        for j in range(n,val-1,-1):
            dp[j]=(dp[j]+dp[j-val])%mod
    return dp[n]

print(numberOfWays(n, x))  # Output: 1