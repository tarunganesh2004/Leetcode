arr=[2,4,6,8,10]

def cumulativeSum(arr):
    n=len(arr)
    prefixSum=[0]*n
    prefixSum[0]=arr[0]

    for i in range(1,n):
        prefixSum[i]=prefixSum[i-1]+arr[i]
    
    # print(prefixSum)
    return prefixSum

def get_range_sum(prefixSum,l,r):
    if l==0:
        return prefixSum[r]
    return prefixSum[r]-prefixSum[l-1]


prefixSum=cumulativeSum(arr)
print(get_range_sum(prefixSum,1,3)) # 18