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

print(subarraySum(nums,t)) # 2