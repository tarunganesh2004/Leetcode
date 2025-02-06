# Rotate Array LC 189

# Given an array, rotate the array to the right by k steps, where k is non-negative.

nums=[1,2,3,4,5,6,7]
k=3

def rotate(nums,k):
    k=k%len(nums)
    nums[:]=nums[-k:]+nums[:-k]
    return nums

# using recursion 
def rotatebyK(nums,k):
    n=len(nums)
    k=k%n
    def reverse(nums,left,right):
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
    reverse(nums,0,n-1)
    reverse(nums,0,k-1)
    reverse(nums,k,n-1)
    return nums

# print(rotate(nums,k))

print(rotatebyK(nums,k))