def threeSum(nums):
    nums.sort()
    res=[]
    n=len(nums)

    for i in range(n-2):

        if i>0 and nums[i]==nums[i-1]:
            continue

        l,r=i+1,n-1  # noqa: E741
        
        while l<r:
            t=nums[i]+nums[l]+nums[r]

            if t<0:
                l+=1  # noqa: E741
            elif t>0:
                r-=1
            else:
                res.append((nums[i],nums[l],nums[r]))

                while l<r and nums[l]==nums[l+1]:
                    l+=1  # noqa: E741
                while l<r and nums[r]==nums[r-1]:
                    r-=1
                
                l+=1  # noqa: E741
                r-=1
    
    return set(res)

a=[-1,0,1,2,-1,-4]
print(threeSum(list(a))) # {(-1, -1, 2), (-1, 0, 1)}
