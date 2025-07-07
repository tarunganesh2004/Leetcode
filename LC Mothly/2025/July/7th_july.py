# Maximum Number of Events That Can Be Attended LC 1353

import heapq
events= [[1,2],[2,3],[3,4]]
def maxEvents(events):
    # using Min heap 
    events.sort()
    heap=[]
    day=1
    i=0
    res=0
    n=len(events)
    while i<n or heap:
        while i<n and events[i][0]<=day:
            heapq.heappush(heap,events[i][1])
            i+=1
        if heap:
            heapq.heappop(heap)
            res+=1
        day+=1
        while heap and heap[0]<day:
            heapq.heappop(heap)
    return res    

print(maxEvents(events))  # Output: 3