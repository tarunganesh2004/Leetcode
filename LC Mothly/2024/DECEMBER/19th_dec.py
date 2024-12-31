# LC 769 Max Chunks To Make Sorted

# Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of "chunks" (partitions), and individually sort each chunk. After concatenating them, the result equals the sorted array.
# What is the most number of chunks we could have made?

arr=[4,3,2,1,0]

def maxChunksToSorted(arr):
    n=len(arr)
    chunks=0
    max_val=0
    for i in range(n):
        max_val=max(max_val,arr[i])
        if max_val==i:
            chunks+=1
    return chunks

print(maxChunksToSorted(arr)) # 1