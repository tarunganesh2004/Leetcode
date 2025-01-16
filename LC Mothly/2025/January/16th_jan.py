# Bitwise XOR of all pairings LC 2425

# You are given two 0-indexed arrays, nums1 and nums2, consisting of non-negative integers. 
# There exists another array, nums3, which contains the bitwise XOR of all pairings of integers between nums1 and nums2 (every integer in nums1 is paired with every integer in nums2 exactly once).

# Return the bitwise XOR of all integers in nums3.

nums1=[2,1,3]
nums2=[10,2,5,0]

# the idea is if both lists have even length then all elements in both lists cancel each other out
# if one list has even length , xor of all elements in odd length list is the answer
# if both lists have odd length then xor of all elements in both lists is the answer

# TC O(n+m) SC O(1)

def xorAllNums(nums1,nums2):
    n1=len(nums1)
    n2=len(nums2)

    if n1%2==0 and n2%2==0:
        return 0
    
    ans=0
    if n2%2==1:
        for i in range(n1):
            ans^=nums1[i]

    if n1%2==1:
        for i in range(n2):
            ans^=nums2[i]
    return ans

print(xorAllNums(nums1,nums2)) 