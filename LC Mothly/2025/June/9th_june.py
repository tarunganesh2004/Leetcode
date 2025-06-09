# Kth Smallest in Lexicographical Order LC 440

n=13
k=2

def findKthNumber(n, k):
    def count_steps(prefix, n):
        steps = 0
        first = prefix
        last = prefix + 1
        while first <= n:
            steps += min(n + 1, last) - first
            first *= 10
            last *= 10
        return steps

    current = 1
    k -= 1  # We start with the first number already counted

    while k > 0:
        steps = count_steps(current, n)
        if steps <= k:
            current += 1
            k -= steps
        else:
            current *= 10
            k -= 1

    return current

print(findKthNumber(n, k))  # Output: 10