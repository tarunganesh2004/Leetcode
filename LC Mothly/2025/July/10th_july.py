# Reschedule Meetings for Maximum Free Time II LC 3440

eventTime=5
startTime=[1,3]
endTime=[2,5]

def maxFreeTime(eventTime,startTime,endTime):
    startTime+=[eventTime]
    endTime=[0]+endTime
    n=len(startTime)
    maxGap=0

    gaps=[0]*n
    for i in range(n):
        gaps[i] = startTime[i] - endTime[i]
    
    leftMax=gaps[:]
    for i in range(1,n):
        leftMax[i]=max(leftMax[i], leftMax[i-1])
    
    rightMax=gaps[:]
    for i in range(n-2,-1,-1):
        rightMax[i]=max(rightMax[i], rightMax[i+1])
    
    for i in range(1,n):
        if (i-2>=0 and endTime[i]-startTime[i-1]<=leftMax[i-2]) or (i+1<=n-1 and endTime[i]-startTime[i-1]<=rightMax[i+1]):
            maxGap=max(maxGap,gaps[i]+gaps[i-1]+endTime[i]-startTime[i-1]) 
        else:
            maxGap=max(maxGap,gaps[i]+gaps[i-1])
    return maxGap


print(maxFreeTime(eventTime, startTime, endTime))