# LC 560
nums=[1,1,1,1,1,1]
t=3

def subarraySum(nums,k):
    m={0:1}
    prefixSum=0
    count=0

    for i in range(len(nums)):
        prefixSum+=nums[i]

        if prefixSum-k in m:
            count+=m[prefixSum-k]
        

        if prefixSum in m:
            m[prefixSum]+=1
        else:
            m[prefixSum]=1

    return count

def printSubarrayswithsumk(arr,k):
    prefix_map={0:[-1]} # initialize with 0 sum at index -1
    prefix_sum=0
    subarrays=[]
    for i,num in enumerate(arr):
        # update prefix_sum
        prefix_sum+=num

        # check if prefix_sum-k exists in prefix_map
        if prefix_sum-k in prefix_map:
            # get all the indices where prefix_sum-k exists
            start_indices=prefix_map[prefix_sum-k]
            for start_index in start_indices:
                subarrays.append(arr[start_index+1:i+1])

        # update prefix_map
        if prefix_sum in prefix_map:
            prefix_map[prefix_sum].append(i)
        else:
            prefix_map[prefix_sum]=[i]

    return subarrays


print(subarraySum(nums,t)) # 2
nums1=[3,4,7,2,-3,1,4,2]
t1=7
print(printSubarrayswithsumk(nums1,t1)) 