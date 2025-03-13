# Zero Array Transformation II LC 3356

nums=[2,0,2]
queries=[[0,2,1],[0,2,1],[1,1,3]]

def minZeroArray(nums,queries):
    n=len(nums)
    total_sum=0
    k=0
    diff=[0]*(n+1)

    for i in range(n):
        while total_sum+diff[i]<nums[i]:
            k+=1

            if k>len(queries):
                return -1
            
            left,right,val=queries[k-1]

            if right>=i:
                diff[max(left,i)]+=val
                diff[right+1]-=val

        total_sum+=diff[i]

    return k

print(minZeroArray(nums,queries))