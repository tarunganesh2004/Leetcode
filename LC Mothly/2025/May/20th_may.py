# Zero Array Transformation I LC 3355

nums=[1,0,1]
queries=[[0,2]]

def isZeroArray(nums, queries):
    n=len(nums)
    freq=[0]*n

    for q in queries:
        freq[q[0]]+=1
        if q[1]+1<n:
            freq[q[1]+1]-=1

    curFreq=0
    for i in range(n):
        curFreq+=freq[i]
        if curFreq<nums[i]:
            return False
    return True

print(isZeroArray(nums, queries))  # Output: True