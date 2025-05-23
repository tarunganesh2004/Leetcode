# Find the Maximum sum of Node Values LC 3068(Hard)

nums=[1,2,1]
k=3
edges=[[0,1],[0,2]]

def maximumValueSum(nums,k,edges):
    res=c=0
    d=1<<30
    for a in nums:
        res+=max(a,b:=a^k)
        c^=a<b
        d=min(d,abs(a-b))

    return res-d*c

print(maximumValueSum(nums,k,edges))