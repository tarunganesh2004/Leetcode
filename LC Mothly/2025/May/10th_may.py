# Minimum Equal Sum of Two Arrays After replacing zeroes LC 2918

nums1=[3,2,0,1,0]
nums2=[6,5,0]

def minSum(nums1,nums2):
    s1=sum(num if num!=0 else 1 for num in nums1)
    s2=sum(num if num!=0 else 1 for num in nums2)

    if (s1<=s2 and 0 in nums1) or s1==s2:
        return s2
    
    if s1>s2 and 0 in nums2:
        return s1
    
    return -1

print(minSum(nums1,nums2))