# Apply Operations To Maximize score LC 2818



nums=[8,3,9,3,8]
k=2

def maximumScore(nums,k):
    MOD=10**9+7
    n=len(nums)
    upper=max(nums)+1

    # compute prime factor counts(primeScore)
    primeScore=[0]*upper
    for i in range(2,upper):
        if primeScore[i]==0:
            for j in range(i,upper,i):
                primeScore[j]+=1
    
    # monotonic stack for next greater element
    nextGreater=[n]*n
    prevGreaterOrEqual=[-1]*n
    stack=[]

    for i in range(n):
        while stack and primeScore[nums[i]]>primeScore[nums[stack[-1]]]:
            stack.pop()
        prevGreaterOrEqual[i]=stack[-1] if stack else -1
        stack.append(i)

    stack.clear()

    for i in range(n-1,-1,-1):
        while stack and primeScore[nums[i]]>=primeScore[nums[stack[-1]]]:
            stack.pop()
        nextGreater[i]=stack[-1] if stack else n
        stack.append(i)

    sorted_indices=sorted(range(n),key=lambda i:nums[i],reverse=True)

    res=1
    for idx in sorted_indices:
        num=nums[idx]
        operations=min((idx-prevGreaterOrEqual[idx])*(nextGreater[idx]-idx),k)
        res=(res*pow(num,operations,MOD))%MOD
        k-=operations
        if k==0:
            return res
    return res

print(maximumScore(nums, k))