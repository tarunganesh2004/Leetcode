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

print(brute_force(arr)) # 5