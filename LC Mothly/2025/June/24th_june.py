# Find All K distant Indices in an Array LC 2200

nums=[3,4,9,1,3,9,5]
key=9
k=1

def findKDistantIndices(nums, key, k):
    n=len(nums)
    ans=[]
    j=0
    for i,x in enumerate(nums):
        if x==key:
            up=min(n-1,i+k)
            j=max(j,i-k)
            while j<=up:
                ans.append(j)
                j+=1
    return ans

print(findKDistantIndices(nums, key, k)) 