# LC 347 Top K Frequent Elements

nums=[1,1,1,2,2,3]
k=2

# Approach 1: Using Counter
def topKFrequent(nums,k):
    from collections import Counter
    freq=Counter(nums)
    freq_list=[]
    for key in freq:
        freq_list.append((key,freq[key]))
    freq_list.sort(key=lambda x:x[1],reverse=True) # O(nlogn)
    res=[]
    for i in range(k):
        res.append(freq_list[i][0])

    return res

# Approach 2: Using Heap(the idea is to use the min heap and pop the elements if the length of heap is greater than k)
def topKFrequentUsingHeap(nums,k):
    from collections import Counter
    import heapq
    freq=Counter(nums)
    heap=[]
    for key in freq:
        heapq.heappush(heap,(freq[key],key)) # push as tuple
        if len(heap)>k:
            heapq.heappop(heap)
    
    res=[]
    while heap:
        res.append(heapq.heappop(heap)[1])

    return res[::-1] # we can use a max heap to avoid reversing the list(we can use -freq[key] instead of freq[key] in the tuple)

print(topKFrequent(nums,k))
print(topKFrequentUsingHeap(nums,k))