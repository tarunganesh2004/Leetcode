# longest subarray with sum k

arr=[10,5,2,7,1,-10]
k=15

def longestSubarray(arr,k):
    map={}
    cur_sum=0
    max_length=0
    for i,num in enumerate(arr):
        cur_sum+=num
        print(cur_sum)
        if cur_sum==k:
            max_length=i+1 
            print(i,max_length)
        print(cur_sum-k,map)
        if cur_sum-k in map:
            print(i,map[cur_sum-k])
            max_length=max(max_length,i-map[cur_sum-k])
            print(max_length)
        if cur_sum not in map:
            map[cur_sum]=i
            print(map)
    return max_length

print(longestSubarray(arr,k))