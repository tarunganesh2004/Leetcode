# Median of Two sorted arrays LC 4 Hard

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# brute force approach merging two arrays and sorting them and then finding the median

nums1=[1,2]
nums2=[3,4]

def findMedian(nums1,nums2): # TC O(m+nlog(m+n))
    nums1.extend(nums2)
    nums1.sort()

    if len(nums1)%2==0:
        return (nums1[len(nums1)//2]+nums1[len(nums1)//2-1])/2
    else:
        return nums1[len(nums1)//2]

# better approach is to use two pointers and merge the two arrays and then find the median
def BetterApproach(nums1,nums2):
    n=len(nums1)
    m=len(nums2)
    i=0
    j=0

    m1=0
    m2=0

    for count in range(0,(n+m)//2+1):
        m1=m2
        if i!=n and j!=m:
            if nums1[i]<nums2[j]:
                m2=nums1[i]
                i+=1
            else:
                m2=nums2[j]
                j+=1
        elif i<n:
            m2=nums1[i]
            i+=1
        else:
            m2=nums2[j]
            j+=1

    if (n+m)%2==0:
        return (m1+m2)/2
    else:
        return m2
    
print(findMedian(nums1,nums2)) # 2.0
