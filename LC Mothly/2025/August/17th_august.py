# New 21 Game LC 837

n=10
k=1
maxPts=10

def new21Game(n, k, maxPts):
    if k == 0 or n >= k + maxPts:
        return 1.0
    
    dp = [0.0] * (n + 1)
    dp[0] = 1.0
    window_sum = 1.0
    
    for i in range(1, n + 1):
        dp[i] = window_sum / maxPts
        if i < k:
            window_sum += dp[i]
        if i >= maxPts:
            window_sum -= dp[i - maxPts]
    
    return sum(dp[k:n + 1])

print(new21Game(n, k, maxPts))  # Output: 1.0