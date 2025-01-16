# Contiguous Array LC 525

# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

arr1=[0,1,0,1,0,1,1,0]

def findMaxLength(arr):
    map={}
    max_len=0
    cur_sum=0
    for i,num in enumerate(arr):
        cur_sum+=(1 if num==1 else -1)
        if cur_sum==0:
            max_len=i+1
        if cur_sum in map:
            max_len=max(max_len,i-map[cur_sum])

        if cur_sum not in map:
            map[cur_sum]=i

    return max_len

print(findMaxLength(arr1)) # 8