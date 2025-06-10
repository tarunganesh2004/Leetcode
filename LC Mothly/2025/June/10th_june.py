# Maximum Difference Between Even and Odd Frequency I  LC 3442

s="aaaaabbc"

def maxDifference(s):
    from collections import Counter

    freq= Counter(s)
    maxOdd=max(v for v in freq.values() if v % 2 == 1)
    minEven=max(v for v in freq.values() if v % 2 == 0)
    return maxOdd - minEven

print(maxDifference(s))  # Output: 3