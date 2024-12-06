def countSubarrayswithSumgreaterthanK(arr,k):
    map={0:1}
    prefixSum=0
    count=0

    for i in range(len(arr)):
        prefixSum+=arr[i]

        # check how many prefix sums are smaller than prefixSum-k
        for prev_sum in map:
            if prefixSum-prev_sum>k:
                count+=map[prev_sum]
        
        if prefixSum in map:
            map[prefixSum]+=1
        else:
            map[prefixSum]=1
        
    return count

arr=[1,2,3,4,5]
k=5
print(countSubarrayswithSumgreaterthanK(arr,k)) # 8