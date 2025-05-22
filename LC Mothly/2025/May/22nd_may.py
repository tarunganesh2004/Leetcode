# Zero Array Transformation III LC 3362

nums=[2,0,2]
queries=[[0,2],[0,2],[1,1]]

def maxRemoval(nums,queries):
    import heapq
    from collections import deque
    q=deque(sorted(queries))
    c=0
    sub=[0 for _ in range(len(nums)+1)]
    usedCount=0
    heap=[]
    for i in range(len(nums)):
        c-=sub[i]
        while q and q[0][0]==i:
            heapq.heappush(heap,-q.popleft()[1])
        while nums[i]>c:
            if not heap:
                return -1
            last=-heapq.heappop(heap)
            if last<i:
                continue
            else:
                c+=1
                sub[last+1]+=1
                usedCount+=1
    return len(queries)-usedCount

print(maxRemoval(nums,queries))