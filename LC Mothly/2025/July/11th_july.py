# Meeting Rooms III LC 2402(Hard)

n = 2
meetings = [[0,10],[1,5],[2,7],[3,4]]

def mostBooked(n,meetings):
    import heapq 
    meetings.sort()
    ready_room=list(range(n))
    meeting_room=[]
    heapq.heapify(ready_room)
    heapq.heapify(meeting_room)

    ans=[0]*n
    for start, end in meetings:
        while meeting_room and meeting_room[0][0]<=start:
            _,room= heapq.heappop(meeting_room)
            heapq.heappush(ready_room, room)
        if ready_room:
            room = heapq.heappop(ready_room)
            heapq.heappush(meeting_room, (end, room))
        else:
            endTime,room= heapq.heappop(meeting_room)
            heapq.heappush(meeting_room, (endTime + (end - start), room))
        ans[room] += 1
    return ans.index(max(ans))

print(mostBooked(n, meetings))  # Output: 0