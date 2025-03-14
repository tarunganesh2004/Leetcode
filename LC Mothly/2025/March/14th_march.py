# Maximum Candies Allocated to K Children LC 2226

candies=[5,8,6]
k=3

def maxCandies(candies,k):
    if sum(candies)<k:
        return 0
    n=len(candies)
    left=1
    right=max(candies)
    ans=0
    while left<=right:
        numOfPiles=0
        mid=(left)+(right-left)//2

        for i in range(n):
            numOfPiles+=candies[i]//mid

        if numOfPiles>=k:
            ans=max(ans,mid)
            left=mid+1
        else:
            right=mid-1

    return ans


print(maxCandies(candies,k))