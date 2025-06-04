# Maximum Candies You Can Get From Boxes LC 1298(Hard)

import collections


status=[1,0,1,0]
candies=[7,5,4,100]
keys = [[], [], [1], []]
containedBoxes=[[1,2],[3],[],[]]
initialBoxes=[0]

def maxCandies(status, candies, keys, containedBoxes, initialBoxes):
    n=len(status)
    can_open=[status[i] == 1 for i in range(n)]
    has_box,used=[False] * n, [False] * n

    q=collections.deque()
    ans=0
    for box in initialBoxes:
        has_box[box] = True
        if can_open[box]:
            q.append(box)
            used[box] = True
            ans += candies[box]

    while len(q)>0:
        box = q.popleft()
        for key in keys[box]:
            can_open[key] = True
            if has_box[key] and not used[key]:
                q.append(key)
                used[key] = True
                ans += candies[key]
        
        for next_box in containedBoxes[box]:
            has_box[next_box] = True
            if can_open[next_box] and not used[next_box]:
                q.append(next_box)
                used[next_box] = True
                ans += candies[next_box]
    return ans

print(maxCandies(status, candies, keys, containedBoxes, initialBoxes))  # Output: 16