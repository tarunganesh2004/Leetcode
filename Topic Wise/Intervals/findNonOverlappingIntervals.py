# Find non overlapping intervals among a list of intervals

intervals = [[1,3],[2,4],[3,5],[7,9]]

def findNonOverlapping(intervals):
    intervals.sort(key=lambda x:x[0])

    nonOverlapping=[]
    n=len(intervals)

    

print(findNonOverlapping(intervals))
