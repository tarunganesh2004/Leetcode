# Square Root of x LC 69

x=8

# Method 1
print(int(x**0.5))

# Method 2 using binary search
def mySqrt(x):
    if x==0:
        return 0
    left=1
    right=x
    while left<=right:
        mid=left+(right-left)//2
        if mid*mid==x:
            return mid
        elif mid*mid<x:
            left=mid+1
        else:
            right=mid-1
    return right

print(mySqrt(x))