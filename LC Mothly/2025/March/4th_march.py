# Check if Number is a sum of powers of Three LC 1780

n=12
def checkPowersOfThree(n):
    while n>1:
        if n%3==2:
            return False
        n//=3
    return n==1

print(checkPowersOfThree(n))