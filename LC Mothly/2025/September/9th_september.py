# Number of Peopl Aware of a Secret LC 2327


n=6
delay=2
forget=4

def peopleAwareOfSecret(n, delay, forget):
    mod = 10**9 + 7
    dp = [0] * (n + 1)
    dp[1] = 1
    total = 0
    for i in range(2, n + 1):
        if i - delay >= 1:
            total += dp[i - delay]
        if i - forget >= 1:
            total -= dp[i - forget]
        dp[i] = total % mod
    return sum(dp[n - forget + 1:]) % mod

print(peopleAwareOfSecret(n, delay, forget))