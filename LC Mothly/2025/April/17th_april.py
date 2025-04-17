# Count Equal and Divisble Pairs in an Array  LC 2176

nums=[3,1,2,2,2,1,3]
k=2

def bruteForce(nums,k):
    n=len(nums)
    cnt=0
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]==nums[j] and i*j%k==0:
                cnt+=1
    return cnt

print(bruteForce(nums,k))