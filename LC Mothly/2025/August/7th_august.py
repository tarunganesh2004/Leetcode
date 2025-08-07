# Find the Maximum Number of Fruits Collected LC 3363(Hard)

fruits = [[1, 2, 3, 4], [5, 6, 8, 7], [9, 10, 11, 12], [13, 14, 15, 16]]

def maxCollectedFruits(fruits):
    n=len(fruits)
    res=0

    for i in range(n):
        res+=fruits[i][i]
    
    def dist(x,y,m):
        return max(n-1-x,n-1-y)==n-1-m
    
    cache={}
    def child(i,j,m,dirs):
        nonlocal n 
        if (i,j) in cache:
            return cache[(i,j)]
        if i==j==n-1:
            return 0
        ans=0
        for x,y in dirs:
            if 0<=i+x<n and 0<=j+y<n and dist(i+x,j+y,m+1):
                v=fruits[i][j] if i!=j else 0
                ans=max(ans,v+child(i+x,j+y,m+1,dirs))
        cache[(i,j)]=ans
        return ans
    res+=child(n-1,0,0,[[1,1],[-1,1],[0,1]])
    res+=child(0,n-1,0,[[1,-1],[1,0],[1,1]])
    return res

print(maxCollectedFruits(fruits))  # Output: 100