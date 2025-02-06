# Merge Sorted Array LC 88

nums1=[1,2,3,0,0,0]
m=3
nums2=[2,5,6]
n=3

def merge(nums1,m,nums2,n):
    nums1[m:]=nums2
    nums1.sort()
    return nums1 # bruteforce

# using two pointers
def mergeOptimized(nums1,m,nums2,n):
    i=m-1
    j=n-1
    k=m+n-1
    while j>=0:
        if i>=0 and nums1[i]>nums2[j]:
            nums1[k]=nums1[i]
            i-=1
        else:
            nums1[k]=nums2[j]
            j-=1
        k-=1
    return nums1

print(merge(nums1,m,nums2,n))
print(mergeOptimized(nums1,m,nums2,n))