# Power of Four LC 342

n = 16

def isPowerOfFour(n):
    if n<=0:
        return False
    while n % 4 == 0:
        n //= 4
    return n == 1
print(isPowerOfFour(n))  # Output: True