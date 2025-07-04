# Subarrays With K Distinct Integers LC 992(Hard)

# exactly k=atmost k - at most k-1

nums = [1, 2, 1, 2, 3]
k = 2


def subarraysWithKDistinct(nums, k):
    def atMostK(k):
        from collections import defaultdict

        count = defaultdict(int)
        left = 0
        subarray_count = 0

        for right in range(len(nums)):
            count[nums[right]] += 1

            while len(count) > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1

            subarray_count += right - left + 1

        return subarray_count

    return atMostK(k) - atMostK(k - 1)


print(
    subarraysWithKDistinct(nums, k)
)  # Output: 7 (subarrays: [1,2], [1,2,1], [2,1,2], [1,2,3], [2,3], [1,2,1,2], [2,1,2,3])
