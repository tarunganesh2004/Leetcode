# # Count the Number of Good Subarrays LC 2537

# Given an integer array nums and an integer k, return the number of good subarrays of nums.

# A subarray arr is good if there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

# A subarray is a contiguous non-empty sequence of elements within an array

nums=[3,1,4,3,2,2,4]
k=2

# brute force
def brute_force(nums):
    # def is_good(subarray,k): # this takes O(n^4)
    #     pairs=0
    #     n=len(subarray)
    #     for i in range(n):
    #         for j in range(i+1,n):
    #             if subarray[i]==subarray[j]:
    #                 pairs+=1
    #                 if pairs>=k:
    #                     return True
    #     return False
    n=len(nums)
    # generating all subarrays
    subarrays=[]
    for i in range(n):
        for j in range(i,n):
            subarrays.append(nums[i:j+1])
    # counting good subarrays
    count=0
    def isGood(subarray,k): # using map takes O(n^3)
        freq={}
        pairs=0
        for val in subarray:
            if val in freq:
                pairs+=freq[val]
                freq[val]+=1
            else:
                freq[val]=1
            if pairs>=k:
                return True
        return False
    
    for subarray in subarrays:
        if isGood(subarray,k):
            count+=1

    return count



print(brute_force(nums))