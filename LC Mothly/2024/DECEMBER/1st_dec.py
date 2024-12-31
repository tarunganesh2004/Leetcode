# Check if N and its double exist 

arr=[10,2,5,3]

def checkIfExist(arr):
    n=len(arr)
    s=set()
    for i in range(n):
        if arr[i]*2 in s or arr[i]/2 in s:
            return True
        s.add(arr[i])
    return False

print(checkIfExist(arr))