# Maximum Candies Allocated to K Children LC 2226

candies=[5,8,6]
k=3

def maxCandies(candies,k):
    n = len(candies)
    left = 1  # the least number of candy in each stack we can give to each student is one
    right = max(candies)  # the max number of candy in each stack that we can give to each student is the maximum number in the candies array
    ans = 0 # ans here is used to store the maximum amount in each stack that we can give to each children. 
               # If we don't have enough to distribute, we will return 0 at the end so we initialize it to be 0 now.

    while left <= right:  # binary search
        numberOfPiles = 0
        mid = (left) + (right - left) // 2  # the number of candies we require to form a stack

        for i in range(n):   # loop through the array to find the numbers of stack we can form
            numberOfPiles += candies[i] // mid   # we add to the numberOfPiles whenever we find that this current stack (candies[i]) can be split into mid (the number of candies we require to form a stack)

        if numberOfPiles >= k: # if our number of piles is greater or equal than the students we have, so we have enough to distribute
            ans = max(ans, mid)   # we first store the max no. of candies in each stack that we can give to each student 
            left = mid + 1      # we will try to increase the number of candies in each stack that we can give to each student
        else: 
            right = mid - 1   # we will try to reduce the number of candies in each stack that we can give to each student
    return ans

# optimized way(another solution)
def maxCandiesAnother(candies,k):
    def isPossible(max_candies):
        res=0
        for candy in candies:
            res+=candy//max_candies
        if res>=k:
            return True
        return False
    
    if sum(candies)<k:
        return 0
    
    left,right=1,sum(candies)//k
    while left<right:
        mid=(left+right)//2+1
        if isPossible(mid):
            left=mid
        else:
            right=mid-1
    return left
    

print(maxCandies(candies,k))
print(maxCandiesAnother(candies,k))