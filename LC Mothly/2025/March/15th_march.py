# # House Robber IV LC 2560

# The capability of the robber is the maximum amount of money he steals from one house of all the houses he robbed.

# You are given an integer array nums representing how much money is stashed in each house. More formally, the ith house from the left has nums[i] dollars.

# You are also given an integer k, representing the minimum number of houses the robber will steal from. It is always possible to steal at least k houses.

# Return the minimum capability of the robber out of all the possible ways to steal at least k houses.


def minCapability(nums, k):
    def check(cap):
        count = 0
        taken = False
        for x in nums:
            if taken:
                taken = False  # Skip adjacent house
            elif x <= cap:
                count += 1
                taken = True  # Mark this house as robbed
            if count >= k:
                return True  # Successfully robbed at least k houses
        return False  # Not enough houses robbed

    left, right = min(nums), max(nums)  # Search space for capability
    while left < right:
        mid = (left + right) // 2
        if check(mid):
            right = mid  # Try to lower capability
        else:
            left = mid + 1  # Increase capability
    return left  # Minimum valid capability


# Test case
nums = [2, 3, 5, 9]
k = 2
print(minCapability(nums, k))  # Output: 5
