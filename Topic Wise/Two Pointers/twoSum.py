from typing import List,Dict


class Solution:
    def twoSum(self,nums:List[int], target:int) -> List[int]: # type: ignore
        map : Dict[int,int]={}
        for i in range(len(nums)):
            c=target-nums[i]
            if c in map:
                return [map[c],i]
            map[nums[i]]=i
        return []
    
if __name__ == "__main__":
    s=Solution()
    print(s.twoSum([2,7,11,15],9))
