# Bitwise ORs of Subarrays LC 898

arr=[1,1,2]

def bruteForce(arr):
    n = len(arr)
    ans = set()
    for i in range(n):
        curr_or = 0
        for j in range(i, n):
            curr_or |= arr[j]
            ans.add(curr_or)
    return len(ans)

# optimized
def subarrayBitwiseORs(arr):
    s=set(arr)
    prev=set()
    prev.add(arr[0])
    for num in arr[1:]:
        temp=set()
        for p in prev:
            temp.add(p | num)
            s.add(num|p)
        prev=temp
        prev.add(num)
    return len(s)

print(bruteForce(arr))
print(subarrayBitwiseORs(arr))