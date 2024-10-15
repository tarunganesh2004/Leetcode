def _4Sum(nums,target):
    nums.sort()
    res=set()
    n=len(nums)

    for i in range(n-3):
            
            if i>0 and nums[i]==nums[i-1]:
                continue
    
            for j in range(i+1,n-2):
    
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
    
                l,r=j+1,n-1  # noqa: E741

                while l<r:
                    t=nums[i]+nums[j]+nums[l]+nums[r]
    
                    if t<target:
                        l+=1
                    elif t>target:
                        r-=1
                    else:
                        res.add((nums[i],nums[j],nums[l],nums[r]))
    
                        while l<r and nums[l]==nums[l+1]:
                            l+=1
                        while l<r and nums[r]==nums[r-1]:
                            r-=1
                            
                        l+=1  # noqa: E741
                        r-=1
    
    return res

a=[1, 0, -1, 0, -2, 2]
target=0
print(_4Sum(list(a),target)) # {(-2, -1, 1, 2), (-2, 0, 0, 2), (-1, 0, 0, 1)}