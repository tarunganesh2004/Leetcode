# Jump game LC 55

nums=[2,3,1,1,4]

def canJump(nums):
    n=len(nums)
    maxReach=0
    for i in range(n):
        if i>maxReach:
            return False
        maxReach=max(maxReach,i+nums[i])
    return True

def anotherWay(nums):
    f=0
    for n in nums:
        if f<0:
            return False
        elif n>f:
            f=n
        f-=1
    return True

# using dp
def jump(nums):
    n=len(nums)
    dp=[0]*n
    dp[0]=nums[0]
    for i in range(1,n-1):
        if dp[i-1]<i:
            return False
        dp[i]=max(dp[i-1],i+nums[i])
        if dp[i]>=n-1:
            return True
        
    return dp[n-2]>=n-1

print(canJump(nums))
print(anotherWay(nums))
print(jump(nums))