intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

def insert(intervals,newInterval):
    intervals.append(newInterval)
    intervals.sort(key=lambda x:x[0])

    merged=[intervals[0]]

    for i in range(1,len(intervals)):
        if merged[-1][1]>=intervals[i][0]:
            merged[-1][1]=max(merged[-1][1],intervals[i][1])
        else:
            merged.append(intervals[i])

    return merged

print(insert(intervals,newInterval))