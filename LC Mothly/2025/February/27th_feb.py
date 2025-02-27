# Length of Longest fibonacci subsequence LC 873
arr=[1,2,3,4,5,6,7,8]

# brute force approach
# check all pairs of i,j and then check if i+j is present in the array

def brute_force(arr):
    n=len(arr)
    s=set(arr)
    res=0
    for i in range(n):
        for j in range(i+1,n):
            a,b=arr[i],arr[j]
            l=2  # noqa: E741
            while a+b in s:
                a,b=b,a+b
                l+=1  # noqa: E741
            res=max(res,l)
    return res

# using recursion
def recursive_fib(arr):
    s=set(arr)
    def helper(a,b):
        if a+b not in s:
            return 2
        return 1+helper(b,a+b)
    res=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            res=max(res,helper(arr[i],arr[j]))
    return res

# using dp (hashmap)
def optimized(arr):
    idx={x:i for i,x in enumerate(arr)} # value to index mapping
    dp={}
    res=0

    for k in range(len(arr)):
        for j in range(k):
            i=idx.get(arr[k]-arr[j]) # find i where arr[i]+arr[j]=arr[k]
            if i is not None and i<j:
                dp[(j,k)]=dp.get((i,j),2)+1 # extend the sequence
                res=max(res,dp[(j,k)])

    return res if res>2 else 0

print(brute_force(arr)) # 5
print(recursive_fib(arr)) # 5

print(optimized(arr)) # 5