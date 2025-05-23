# Count Days Without Meetings LC 3169


days=10
meetings=[[5,7],[1,3],[9,10]]

# brute force
def bruteForce(days,meetings): 
    arr=[]
    for i in range(len(meetings)):
        for j in range(meetings[i][0],meetings[i][1]+1):
            arr.append(j)
    
    c=0
    for i in range(1,days+1):
        if i not in arr:
            c+=1
    return c

# using set(memory limit exceeded)
def countDaysWithoutMeetings(days,meetings):
    meetingDays=set()
    for start,end in meetings:
        for i in range(start,end+1):
            meetingDays.add(i)
    
    return len(set(range(1,days+1))-meetingDays)

# using sorting
def countDays(days,meetings):
    free_days=0
    latest_end=0

    meetings.sort()
    for start,end in meetings:
        if start>latest_end:
            free_days+=start-latest_end-1
        latest_end=max(latest_end,end)

    free_days+=days-latest_end
    return free_days

# another simple approach(similar to merge intervals)
def anotherWay(days,meetings):
    meetings.sort(key=lambda x:x[0])
    count=meetings[0][0]-1
    n=len(meetings)
    for i in range(1,n):
        if meetings[i][0]<=meetings[i-1][1]:
            if meetings[i][1]<=meetings[i-1][1]:
                meetings[i][1]=meetings[i-1][1]
        else:
            dy=meetings[i][0]-meetings[i-1][1]
            count+=dy-1
    count+=days-meetings[n-1][1]
    return count

print(bruteForce(days,meetings))
print(countDaysWithoutMeetings(days,meetings))
print(countDays(days,meetings))
print(anotherWay(days,meetings))