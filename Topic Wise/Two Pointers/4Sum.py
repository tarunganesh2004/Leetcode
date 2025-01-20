# 4 Sum LC 18

a=[1, 0, -1, 0, -2, 2]
target=0

# brute force approach is to use 4 nested loops 
def bruteforce(arr,target): # O(n^5) time complexity
    res=[]
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):  # noqa: E741
                    if arr[i]+arr[j]+arr[k]+arr[l]==target:
                        cur=[arr[i],arr[j],arr[k],arr[l]]
                        cur.sort()
                        if cur not in res:
                            res.append(cur)
    return res

# Better approach is to use a hashmap to store the sum of 2 elements and then check if the negative of the sum of the other 2 elements is in the hashmap
def fourSumUsingHashing(arr,target):
    res_set=set() # O(n^3) time complexity & O(n) space complexity
    n=len(arr)

    for i in range(n):
        for j in range(i+1,n):
            s=set()
            for k in range(j+1,n):
                sum_val=arr[i]+arr[j]+arr[k]
                last=target-sum_val
                if last in s:
                    cur=sorted([arr[i],arr[j],arr[k],last])
                    res_set.add(tuple(cur))
                s.add(arr[k])
    return [list(x) for x in res_set]

def fourSumOptimized(arr,target):
    n=len(arr) # O(n^3) time complexity & O(1) space complexity
    arr.sort()
    res=[]
    for i in range(n):
        # skip duplicates for i
        if i>0 and arr[i]==arr[i-1]:
            continue
        for j in range(i+1,n):
            # skip duplicates for j
            if j>i+1 and arr[j]==arr[j-1]:
                continue
            left=j+1
            right=n-1
            # Two pointer approach
            while left<right:
                total=arr[i]+arr[j]+arr[left]+arr[right]
                if total==target:
                    res.append([arr[i],arr[j],arr[left],arr[right]])
                    # skip duplicates for left
                    while left<right and arr[left]==arr[left+1]:
                        left+=1
                    # skip duplicates for right
                    while left<right and arr[right]==arr[right-1]:
                        right-=1
                    left+=1
                    right-=1
                
                # if total is less than target, increment left
                elif total<target:
                    left+=1
                # if total is greater than target, decrement right
                else:
                    right-=1
    return res


print(bruteforce(a,target)) # [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
print(fourSumUsingHashing(a,target)) # [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
print(fourSumOptimized(a,target)) # [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]