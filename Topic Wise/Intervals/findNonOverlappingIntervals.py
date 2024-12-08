# Find non overlapping intervals among a list of intervals

intervals = [[1,3],[2,4],[3,5],[7,9]]

def findNonOverlapping(intervals):
    intervals.sort(key=lambda x:x[0])

    nonOverlapping=[]
    n=len(intervals)
    if n<1:
        return
    
    for i in range(1,n):
        prevEnd=intervals[i-1][1]
        print(prevEnd)
        currStart=intervals[i][0]
        print(currStart)
        if prevEnd<currStart:
            nonOverlapping.append([prevEnd,currStart])

    # for i in nonOverlapping:
    #     print(i)

    return nonOverlapping
print(findNonOverlapping(intervals))
