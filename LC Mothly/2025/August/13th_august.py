# Power of Three LC 326

n=27

def isPowerOfThree(n):
    if n<=0:
        return False
    while n%3==0:
        n //= 3
    return n==1

print(isPowerOfThree(n))  