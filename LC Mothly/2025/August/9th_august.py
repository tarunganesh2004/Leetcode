# Power of Two LC 231

n=1

def isPowerOfTwo(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

print(isPowerOfTwo(n))  