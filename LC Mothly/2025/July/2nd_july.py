# Find the Original Typed String II LC 3333

word="aabbccdd"
k=7

def possibleStringCount(word, k):
    MOD=10**9 + 7
    if not word:
        return 0
    
    groups=[]
    count=1
    for i in range(1, len(word)):
        if word[i] == word[i-1]:
            count += 1
        else:
            groups.append(count)
            count = 1
    groups.append(count)

    total=1
    for i in groups:
        total=(total*i) % MOD

    if k<=len(groups):
        return total
    
    dp=[0]*(k)
    dp[0]=1
    for i in groups:
        dps=[0]*(k)
        sm=0
        for s in range(k):
            if s>0:
                sm=(sm+dp[s-1]) % MOD
            if s>i:
                sm=(sm-dp[s-i-1]+MOD) % MOD
            dps[s]=sm 
        dp=dps

    invalid=sum(dp[len(groups):])%MOD
    return (total - invalid + MOD) % MOD

print(possibleStringCount(word, k))  # Output: 5