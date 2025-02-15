# Product of Array Except Self LC 238

arr=[1,2,3,4]

def productExceptSelf(arr):
    n=len(arr)
    prefix=[1]*n
    suffix=[1]*n
    output=[1]*n
    # prefix
    for i in range(1,n):
        prefix[i]=prefix[i-1]*arr[i-1]
    # suffix
    for i in range(n-2,-1,-1):
        suffix[i]=suffix[i+1]*arr[i+1]
    # output
    for i in range(n):
        output[i]=prefix[i]*suffix[i]
    return output

# space optimized approach
def optimized(arr):
    n=len(arr)
    output=[1]*n
    # prefix
    for i in range(1,n):
        output[i]=output[i-1]*arr[i-1]
    # suffix
    suffix=1
    for i in range(n-1,-1,-1):
        output[i]=output[i]*suffix
        suffix=suffix*arr[i]
    return output


print(productExceptSelf(arr))