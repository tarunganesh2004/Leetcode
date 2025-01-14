# Sort Characters By Frequency LC 451

from collections import Counter
import heapq

s="tree" # eert

# Approach 1 using counter and sort
# O(nlogn) & O(n)

def frequencySort(s):
    count=Counter(s)
    res=""
    # most_common() returns a list of tuples with the most common elements
    chr_list=[]
    for k,v in count.most_common():
        chr_list.append((k,v))
    # sort by descending order of frequency
    chr_list.sort(key=lambda x:x[1],reverse=True)

    for k,v in chr_list:
        res+=k*v
    return res

# Approach 2 using heap O(nlogn) & O(n)
def frequencySortUsingheap(s):
    count=Counter(s)
    res=""
    heap=[]
    for k,v in count.items(): # use max heap
        heapq.heappush(heap,(-v,k))
    while heap:
        v,k=heapq.heappop(heap)
        res+=k*(-v)
    return res

# Approach 3 using bucket sort O(n) & O(n)
def frequencySortOptimized(s):
    count=Counter(s)
    bucket=[[] for i in range(len(s)+1)]
    for k,v in count.items():
        bucket[v].append(k)
    # print(bucket)
    res=""
    for i in range(len(bucket)-1,-1,-1):
        for c in bucket[i]:
            res+=c*i
    return res

print(frequencySort(s)) # eert
print(frequencySortUsingheap(s)) # eert
print(frequencySortOptimized(s)) # eert