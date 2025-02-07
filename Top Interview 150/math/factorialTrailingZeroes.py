# Factorial Trailing Zeroes LC 172

n=3

def trailingZeroes(n):
    count=0
    while n>=5:
        n=n//5
        count+=n
    return count

print(trailingZeroes(n))