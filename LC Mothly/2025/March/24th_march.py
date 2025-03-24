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

print(bruteForce(days,meetings))
print(countDaysWithoutMeetings(days,meetings))