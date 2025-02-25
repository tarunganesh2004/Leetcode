# Number of Sub-arrays with odd sum LC 1524

arr=[1,3,5]

mod=10**9+7
# brute force approach
def numOfSubarraysBrute(arr):
    res=0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if sum(arr[i:j+1])%2!=0:
                res+=1
    return res%mod

# optimized approach is to keep track of odd and even sum till i
def numOfSubarrays(arr):
    odd=0
    even=1
    res=0
    total=0
    for i in range(len(arr)):
        total+=arr[i]
        if total%2==0:
            res+=odd
            even+=1
        else:
            res+=even
            odd+=1
    return res%mod

print(numOfSubarraysBrute(arr)) # 4
print(numOfSubarrays(arr)) # 4