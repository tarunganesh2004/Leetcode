# Build Array From Permutation LC 1920

nums=[0,2,1,5,3,4]

# using O(n) space complexity
def buildArray(nums):
    n = len(nums)
    ans = [0] * n
    for i in range(n):
        ans[i] = nums[nums[i]]
    return ans


# using O(1) space complexity
def buildArrayOptimized(nums):
    n = len(nums)
    for i in range(n):
        nums[i] += (nums[nums[i]] % n) * n
    for i in range(n):
        nums[i] //= n
    return nums

print(buildArray(nums))  # Output: [0,1,2,4,5,3]
print(buildArrayOptimized(nums))  # Output: [0,1,2,4,5,3]