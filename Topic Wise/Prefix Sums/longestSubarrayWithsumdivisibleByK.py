# Longest subarray with sum divisible by k

arr=[2,7,6,1,4,5]
k=3

def longestSubarray(arr,k): # O(n) & O(k)
    map={}
    cur_sum=0
    max_length=0
    res=[]
    for i,num in enumerate(arr):
        cur_sum+=num
        mod=cur_sum%k

        if mod<0:
            mod+=k
        if mod==0:
            res.append(arr[:i+1])
            print(f"Subarray: {arr[: i + 1]}")
            max_length=i+1
        if mod in map:
            max_length=max(max_length,i-map[mod][0])
            for start_idx in map[mod]:
                res.append(arr[start_idx+1:i+1])
                print(f"Subarray: {arr[start_idx + 1: i + 1]}")

        if mod not in map:
            map[mod]=[]
        map[mod].append(i)

    return max_length,res

print(longestSubarray(arr,k))