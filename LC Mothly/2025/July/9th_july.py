# Reschedule Meetings for Maximum Free Time I LC 3439

eventTime=5
k=1
startTime=[1,3]
endTime=[2,5]

def maxFreeTime(eventTime, k, startTime, endTime):
    n=len(startTime)
    gaps=[0]*(n+1)

    gaps[0]=startTime[0]
    gaps[n]=eventTime-endTime[-1]
    for i in range(1, n):
        gaps[i] = startTime[i] - endTime[i-1]

    pref=[0]*(n+2)
    for i in range(1, n+2):
        pref[i] = pref[i-1] + gaps[i-1]

    res=0
    for i in range(k+1,n+2):
        res=max(res,pref[i]-pref[i-(k+1)])
    return res

print(maxFreeTime(eventTime, k, startTime, endTime))  