# Kth Smallest Product of Two Sorted Arrays LC 2040(Hard)

nums1=[2,5]
nums2=[3,4]
k=2



class Solution:
    def kthSmallestProduct(self,nums1, nums2, k):
        # Ensure nums1 is the smaller array to reduce iterations
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # Establish binary search boundaries based on product extremes
        products = [
            nums1[0] * nums2[-1],
            nums1[0] * nums2[0],
            nums1[-1] * nums2[0],
            nums1[-1] * nums2[-1],
        ]
        l, r = min(products), max(products)  # noqa: E741

        # Binary search for the k-th smallest product
        while l < r:
            mid = (l + r) // 2
            if (
                self.countLessEqual(nums1, nums2, mid) >= k
            ):  # Check if mid is a valid k-th product
                r = mid
            else:
                l = mid + 1  # noqa: E741
        return l

    # Helper function to count products <= mid
    def countLessEqual(self, nums1, nums2, mid):
        count = 0
        for i in nums1:
            if i < 0:  # Handling negative numbers in nums1
                if nums2[0] * i <= mid:  # All pairs in nums2 are valid
                    count += len(nums2)
                elif nums2[-1] * i > mid:  # All pairs exceed mid
                    continue
                else:  # Binary search for boundary in nums2
                    l, r = 0, len(nums2) - 1  # noqa: E741
                    while l < r:
                        m = (l + r) // 2
                        if nums2[m] * i <= mid:
                            r = m
                        else:
                            l = m + 1  # noqa: E741
                    count += len(nums2) - l

            elif i > 0:  # Handling positive numbers in nums1
                if nums2[-1] * i <= mid:  # All pairs are valid
                    count += len(nums2)
                elif nums2[0] * i > mid:  # All pairs exceed mid
                    continue
                else:  # Binary search for boundary in nums2
                    l, r = 0, len(nums2) - 1  # noqa: E741
                    while l < r:
                        m = (l + r + 1) // 2
                        if nums2[m] * i <= mid:
                            l = m  # noqa: E741
                        else:
                            r = m - 1
                    count += l + 1

            else:  # Special case where element in nums1 is zero
                count += len(nums2) if mid >= 0 else 0

        return count
    
solution = Solution()
print(solution.kthSmallestProduct(nums1, nums2, k))  # Output:8