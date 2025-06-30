# Longest Harmonic Subsequence LC 594

nums=[1,3,2,2,5,2,3,7]

def findLHS(nums):
    from collections import Counter
    
    count = Counter(nums)
    max_length = 0
    
    for num in count:
        if num + 1 in count:
            max_length = max(max_length, count[num] + count[num + 1])
    
    return max_length

print(findLHS(nums))  # Output: 5 (the subsequence [3,2,2,2,3] has length 5)