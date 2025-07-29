# Smallest Subarrays With Maximum Bitwise OR LC 2411

nums=[1,0,2,1,3]

def smallestSubarrays(nums):
    n=len(nums)
    pos=[-1]*31
    ans=[0]*n
    for i in range(n-1,-1,-1):
        j=i
        for bit in range(31):
            if (nums[i]&(1<<bit))==0:
                if pos[bit]!=-1:
                    j=max(j,pos[bit])
            else:
                pos[bit]=i
        ans[i]=j-i+1

    return ans

print(smallestSubarrays(nums))