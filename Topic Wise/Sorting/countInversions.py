# Count Inversions
# count=0
def mergeSort(arr,low,high):
    count=0
    if low>=high:
        return count
    mid=(low+high)//2

    count+=mergeSort(arr,low,mid)
    count+=mergeSort(arr,mid+1,high)
    count+=merge(arr,low,mid,high)
    return count

def merge(arr,low,mid,high):
    left=low
    right=mid+1
    temp=[]
    count=0

    while left<=mid and right<=high:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            count+=mid-left+1
            right+=1
    
    while left<=mid:
        temp.append(arr[left])
        left+=1
    while right<=high:
        temp.append(arr[right])
        right+=1
    
    for i in range(len(temp)):
        arr[low+i]=temp[i]
    return count

def countInversions(arr):
    count=mergeSort(arr,0,len(arr)-1)
    return count
    
arr=[2,4,1,3,5]
print(countInversions(arr))