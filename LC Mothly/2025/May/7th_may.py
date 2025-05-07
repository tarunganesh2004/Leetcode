# # Find the Minimum Time to Reach Last Room I LC 3341

# There is a dungeon with n x m rooms arranged as a grid.

# You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes exactly one second.

# Return the minimum time to reach the room (n - 1, m - 1).

# Two rooms are adjacent if they share a common wall, either horizontally or vertically.

moveTime=[[0,4],[4,4]]

def minTimeToReach(moveTime):
    import heapq
    # using dijkstra's algorithm
    r=len(moveTime)
    c=len(moveTime[0])

    minHeap=[(0,0,0)] #(cur_time,x,y), start with (0,0) at time 0
    arrivalTime=[[float('inf')]*c for _ in range(r)]
    arrivalTime[0][0]=0

    dir=[(0,1),(1,0),(-1,0),(0,-1)] # right, down, up, left
    while minHeap:
        curTime,x,y=heapq.heappop(minHeap)
        if x==r-1 and y==c-1:
            return curTime

        for dx,dy in dir:
            nx,ny=x+dx,y+dy
            if 0<=nx<r and 0<=ny<c:
                waitTime=max(moveTime[nx][ny]-curTime,0) # wait time to enter the room
                newTime=curTime+1+waitTime # 1 sec to move to the next room + wait time
                # if the new time is less than the arrival time, update it
                if newTime<arrivalTime[nx][ny]:
                    arrivalTime[nx][ny]=newTime
                    heapq.heappush(minHeap,(newTime,nx,ny))
    return -1

print(minTimeToReach(moveTime))  # Output: 6