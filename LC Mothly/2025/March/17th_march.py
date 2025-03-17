# # Divide Array Into Equal Pairs LC 2206

# You are given an integer array nums consisting of 2 * n integers.

# You need to divide nums into n pairs such that:

# Each element belongs to exactly one pair.
# The elements present in a pair are equal.
# Return true if nums can be divided into n pairs, otherwise return false.

 

nums=[3,2,3,2,2,2]

def divideArray(nums):
    from collections import Counter
    count=Counter(nums)
    print(count)
    for key in count:
        if count[key]%2!=0:
            return False
    return True

print(divideArray(nums))