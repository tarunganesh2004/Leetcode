# # Design a Number Container System LC 2349

# Design a number container system that can do the following:

# Insert or Replace a number at the given index in the system.
# Return the smallest index for the given number in the system.
# Implement the NumberContainers class:

# NumberContainers() Initializes the number container system.
# void change(int index, int number) Fills the container at index with the number. If there is already a number at that index, replace it.
# int find(int number) Returns the smallest index for the given number, or -1 if there is no index that is filled by number in the system.

import heapq
class NumberContainers:
    def __init__(self):
        self.num_to_index={} # stores number -> min heap of indexes
        self.index_to_num={} # stores index -> number

    def change(self,index,number):
        if index in self.index_to_num:
            old_num=self.index_to_num[index]
            if old_num in self.num_to_index:
                heapq.heappush(self.num_to_index[old_num],float('inf')) #lazy deletion

        # update the index to number mapping
        self.index_to_num[index]=number

        if number not in self.num_to_index:
            self.num_to_index[number]=[]
        heapq.heappush(self.num_to_index[number],index)

    def find(self,number):
        if number not in self.num_to_index or not self.num_to_index[number]:
            return -1
        # return min(self.num_to_index[number]) this takes O(n) time and leads to TLE
        # so we can use a heap to store the indexes
        # remove invalid indexes
        while self.num_to_index[number] and self.index_to_num.get(self.num_to_index[number][0])!=number:
            heapq.heappop(self.num_to_index[number])

        if not self.num_to_index[number]:
            return -1
        return self.num_to_index[number][0]
    
# Space complexity: O(n)

    
# Time complexity: O(1) for change and O(n) for find

N=NumberContainers()
N.change(1,10)
N.change(2,20)
N.change(3,30)
N.change(4,40)
print(N.find(10)) # 1
print(N.find(20)) # 2

# other approach is to use sortedList from sortedcontainers module

# from sortedcontainers import SortedList  # noqa: E402
# from collections import defaultdict  # noqa: E402
# class NumberContainers:
#     def __init__(self):
#         self.num_to_index=defaultdict(SortedList)
#         self.index_to_num={}

#     def change(self,index,number):
#         if index in self.index_to_num:
#             old_num=self.index_to_num[index]
#             self.num_to_index[old_num].remove(index)

#         # update the index to number mapping
#         self.index_to_num[index]=number

#         self.num_to_index[number].add(index)

#     def find(self,number):
#         if number not in self.num_to_index or not self.num_to_index[number]:
#             return -1
#         return self.num_to_index[number][0]
    
