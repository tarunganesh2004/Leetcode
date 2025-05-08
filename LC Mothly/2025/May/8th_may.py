# Find Minimum Time to Reach Last Room II LC 3342

moveTime=[[0,4],[4,4]]

def minTimeToReach(moveTime):
    import heapq
    r=len(moveTime)
    c=len(moveTime[0])
    roomMoveTime=moveTime

    pq=[(0,0,0,1)]
    arrivalTime=[[float('inf')]*c for _ in range(r)]
    arrivalTime[0][0]=0

    dir=[(0,1),(1,0),(-1,0),(0,-1)] # right, down, up, left

    while pq:
        curTime,x,y,curRoom=heapq.heappop(pq)
        if x==r-1 and y==c-1:
            return curTime

        for dx,dy in dir:
            nx,ny=x+dx,y+dy
            if 0<=nx<r and 0<=ny<c:
                waitTime=max(roomMoveTime[nx][ny]-curTime,0)
                newArrivalTime=curTime+curRoom+waitTime # 1 sec to move to the next room + wait time

                if newArrivalTime<arrivalTime[nx][ny]:
                    arrivalTime[nx][ny]=newArrivalTime
                    nextStepCost=1 if curRoom==2 else 2
                    heapq.heappush(pq,(newArrivalTime,nx,ny,nextStepCost))

    return -1

print(minTimeToReach(moveTime))  # Output: 7