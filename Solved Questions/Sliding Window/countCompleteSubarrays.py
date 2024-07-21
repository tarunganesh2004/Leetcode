from collections import defaultdict
from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int: # nums=[1,2,1,3,2]
        # remove duplicates
        distinct=set(nums)
        total_distinct_count=len(distinct)
        n=len(nums)
        left=0 # left pointer
        ans=0
        current_count=defaultdict(int) # default dict to store the count element within the  window
        distinct_in_window=0 # count of distinct elements in the window
        for right in range(n):
            current_count[nums[right]]+=1
            if current_count[nums[right]]==1:
                distinct_in_window+=1

            while distinct_in_window==total_distinct_count:
                ans+=(n-right)
                current_count[nums[left]]-=1
                if current_count[nums[left]]==0:
                    distinct_in_window-=1
                left+=1


        return ans

solution = Solution()
nums = [1, 3,1,2,2]
result = solution.countCompleteSubarrays(nums)
print(result)