# # Count Good Numbers LC 1922

# A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

# For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.

mod=10**9+7

n=1
def countGoodNumbers(n):
    if n==1:
        return 5
    if n==2:
        return 20
    
    # if n is even 5^(n//2) * 4^(n//2)
    # if n is odd 5^(n//2+1) * 4^(n//2+1)
    if n%2==0:
        return (pow(5,n//2,mod)*pow(4,n//2,mod))%mod
    else:
        return (pow(5,n//2+1,mod)*pow(4,n//2,mod))%mod
    
def pow(x,y,p):
    res=1
    x=x%p
    while y>0:
        if y%2==1:
            res=(res*x)%p
        y=y//2
        x=(x*x)%p
    return res

print(countGoodNumbers(n))