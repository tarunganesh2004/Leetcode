# Distribute Candies Among Children II LC 2929




n=5
limit=2

def distributeCandies(n,m):
    def calc(x):
        if x<0:
            return 0
        return x*(x-1)//2
    
    return calc(n+2)-3*calc(n-m+1)+3*calc(n-(m+1)*2+2)-calc(n-3*(limit+1)+2)

print(distributeCandies(n, limit))  # Output: 3