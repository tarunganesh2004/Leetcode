# LC 2466 Count Ways to build good strings

low=3
high=3
zero=1
one=1

def countWaysToBuildRecursiveAproach(low,high,zero,one):
    mod=10**9+7

    def dfs(length):
        if length>high:
            return 0
        
        res=1 if length>=low else 0
        res+=dfs(length+zero)+dfs(length+one)
        
        return res%mod
    
    return dfs(0)

def countWays(low,high,zero,one):
    # Memoization
    mod=10**9+7
    dp={}

    def dfs(length):
        if length>high:
            return 0
        
        if length in dp:
            return dp[length]
        
        dp[length]=1 if length>=low else 0
        dp[length]+=dfs(length+zero)+dfs(length+one)

        return dp[length]%mod
    
    return dfs(0)

def countWaysTabulation(low,high,zero,one):
    mod=10**9+7
    dp={0:1}

    for i in range(1,high+1):
        dp[i]=(dp.get(i-zero,0)+dp.get(i-one,0))%mod

    return sum(dp[i] for i in range(low,high+1))%mod

print(countWaysToBuildRecursiveAproach(low,high,zero,one))
print(countWays(low,high,zero,one))