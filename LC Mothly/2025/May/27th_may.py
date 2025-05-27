# Divisible and Non-divisible sums difference LC 2894

n=10
m=3

def differenceOfSums(n,m):
    s1=0
    s2=0
    for i in range(1,n+1):
        if i % m == 0:
            s2 += i
        else:
            s1 += i
    return s1-s2

# optimized
def optimized(n,m):
    # not divisible - divisible by m 
    # not divisble=total- divisble by m 
    total = n * (n + 1) // 2
    #  from 1 to n, n//m is the count of numbers divisible by m
    k= n // m
    divisible = m * (k * (k + 1)) // 2
    return total-2*divisible

print(differenceOfSums(n,m))
print(optimized(n,m))