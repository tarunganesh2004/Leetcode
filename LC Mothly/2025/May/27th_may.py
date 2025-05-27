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

print(differenceOfSums(n,m))