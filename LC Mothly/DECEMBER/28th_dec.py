# LC 689 Maximum sum of 3 non-overlapping subarrays


nums=[1,2,1,2,6,7,5,1]
k=2

def maxSumOfThreeSubarrays(nums,k):
    # include the sum of the first k elements and skip 

    # preprocessing the array to get the sum of the first k elements
    k_sums=[sum(nums[:k])] 

    # 1 2 3 4 5
    # k=3
    # start at index k
    for i in range(k,len(nums)):
        k_sums.append(k_sums[-1]+nums[i]-nums[i-k])

    dp={}
    def get_max_sum(i,cnt):
        if cnt==3 or i>len(nums)-k:
            return 0
        if (i,cnt) in dp:
            return dp[(i,cnt)]
        
        # include 
        include=k_sums[i]+get_max_sum(i+k,cnt+1)
        # skip
        skip=get_max_sum(i+1,cnt)

        dp[(i,cnt)]= max(include,skip)
        return dp[(i,cnt)]
    
    def get_indices():
        i=0
        indices=[]

        while i<=len(nums)-k and len(indices)<3:
            include=k_sums[i]+get_max_sum(i+k,len(indices)+1)
            skip= get_max_sum(i+1,len(indices))
            if include>=skip:
                indices.append(i)
                i+=k
            else:
                i+=1

        return indices
    
    return get_indices()

print(maxSumOfThreeSubarrays(nums,k))