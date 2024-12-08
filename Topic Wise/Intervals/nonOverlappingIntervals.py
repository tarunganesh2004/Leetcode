"""
Given a list of intervals with starting and ending values, the task is to 
find the minimum number of intervals that are required to be removed to make remaining intervals non-overlapping.
"""

intervals=[[1,2],[2,3],[3,4],[1,3]]

def eraseOverlap(intervals):
    intervals.sort(key=lambda x:x[0])
    n=len(intervals)
    if n<1:
        return 0
    count=0
    end=intervals[0][1]

    for i in range(1,n):
        # print(str(end)+" "+str(intervals[i][0]))
        if intervals[i][0]<end:
            count+=1
            # print(count)
            end=min(end,intervals[i][1])
            # print(end)
        else:
            end=intervals[i][1]
            # print(end)
    return count

print(eraseOverlap(intervals))
    