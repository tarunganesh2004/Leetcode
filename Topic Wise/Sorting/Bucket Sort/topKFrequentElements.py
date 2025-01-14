# Top K frequent Elements LC 347

arr=[1,1,1,2,2,3]
k=2
arr1=[1,2,3,4,5]
# the idea is to use a bucket sort to store the frequency of each element(O(n))

# using index to map the frequency of each element and values to store the elements

def topKFrequent(nums,k): # O(n) & O(n)
    count={}
    bucket=[[] for i in range(len(nums)+1)]
    for i in nums:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    for key,value in count.items():
        bucket[value].append(key)

    print(bucket)
    res=[]
    for i in range(len(bucket)-1,-1,-1):
        for n in bucket[i]:
            res.append(n)
            if len(res)==k:
                return res
    
print(topKFrequent(arr,k)) # [1,2]
print(topKFrequent(arr1,k)) # [1,2]