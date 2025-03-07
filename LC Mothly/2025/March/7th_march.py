# # Closest Prime Numbers in Range LC 2523

# Given two positive integers left and right, find the two integers num1 and num2 such that:

# left <= num1 < num2 <= right .
# Both num1 and num2 are prime numbers.
# num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
# Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].


left=10
right=19

def closestPrimes(left,right): # O(n*sqrt(n)) brute force
    def isPrime(num):
        if num==1:
            return False
        if num==2:
            return True
        if num%2==0:
            return False
        for i in range(3,int(num**0.5)+1,2):
            if num%i==0:
                return False
        return True
    
    primes=[]
    for num in range(left,right+1):
        if isPrime(num):
            primes.append(num)

    min_dif=float('inf')
    ans=[-1,-1]
    for i in range(len(primes)-1):
        if primes[i+1]-primes[i]<min_dif:
            min_dif=primes[i+1]-primes[i]
            ans=[primes[i],primes[i+1]]
    return ans

print(closestPrimes(left,right)) # [11, 13]