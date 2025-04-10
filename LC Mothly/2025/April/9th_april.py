# Minimum Operations to Make Array Values Equal to K LC 3375

nums = [5, 2, 5, 4, 5]
k = 2


def minOperations(nums, k):
    s = set()
    for x in nums:
        if x < k:
            return -1
        elif x > k:
            s.add(x)
    return len(s)


print(minOperations(nums, k))  # 2
