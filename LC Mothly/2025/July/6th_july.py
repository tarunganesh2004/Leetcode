# Finding Pairs with a Certain Sum LC 1865

from collections import Counter


class FindSumPairs:
    def __init__(self,nums1,nums2):
        self.nums1= nums1
        self.nums2= nums2
        self.freq=Counter(nums2)

    def add(self,index,val):
        self.freq[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.freq[self.nums2[index]] += 1

    def count(self,tot):
        count=0
        for num in self.nums1:
            count += self.freq[tot - num]
        return count
    

nums1 = [1, 1, 2, 3]
nums2 = [2, 3, 4, 5]
find_sum_pairs = FindSumPairs(nums1, nums2)
print(find_sum_pairs.count(7))  # Output: 2
find_sum_pairs.add(0, 1)
print(find_sum_pairs.count(7))  # Output: 2
find_sum_pairs.add(1, 1)