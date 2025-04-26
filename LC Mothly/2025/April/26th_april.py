# Count Subarrays With Fixed Bounds LC 2444 (Hard)

nums=[1,3,5,2,7,5]
minK=1
maxK=5

# brute force
def bruteForce(nums,minK,maxK):
    count=0
    n=len(nums)
    for i in range(n):
        for j in range(i,n):
            subarray=nums[i:j+1]
            if min(subarray)==minK and max(subarray)==maxK:
                count+=1
    return count

# optimized approach is to maintain last position of minK and maxK and invalid number(outside the range)
def optimized(nums,minK,maxK):
    ans=0
    min_pos=-1 # last seen position of minK
    max_pos=-1 # last seen position of maxK
    invalid_pos=-1 # last seen position of invalid number

    for i,num in enumerate(nums):
        # if num is out of range,mark invalid
        if num<minK or num>maxK:
            invalid_pos=i

        # track the latest position of minK and maxK
        if num==minK:
            min_pos=i
        if num==maxK:
            max_pos=i

        # count valid subarrays ending at i
        valid=min(min_pos,max_pos)
        if valid>invalid_pos:
            ans+=valid-invalid_pos
    return ans

print(bruteForce(nums,minK,maxK)) # Output: 2
print(optimized(nums,minK,maxK)) # Output: 2