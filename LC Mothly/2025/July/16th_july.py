# Find the Maximum Length of Valid Subsequence I LC 3201

nums=[1,2,3,4]

def maxLength(nums):
    c=nums[0]%2
    odd=even=both=0
    for num in nums:
        if num%2==0:
            even += 1
        else:
            odd += 1
        if num % 2 == c:
            both += 1
            c= 1 - c # toggle c between 0 and 1
    return max(odd, even, both)

print(maxLength(nums))  # Output: 4