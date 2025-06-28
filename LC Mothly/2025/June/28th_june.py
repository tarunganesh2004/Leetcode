# Find Subsequence of Length K With the Largest Sum LC 2099



nums=[2,1,3,3]
k=2

def maxSubsequence(nums,k):
    nums_with_idx = [(num, i) for i, num in enumerate(nums)]

    # sort by value in descending order
    nums_with_idx.sort(key=lambda x:-x[0])

    # take top k and sort by original index
    top_k = sorted(nums_with_idx[:k], key=lambda x: x[1])
    return [num for num, _ in top_k]

print(maxSubsequence(nums, k))  # Output: [3,3]