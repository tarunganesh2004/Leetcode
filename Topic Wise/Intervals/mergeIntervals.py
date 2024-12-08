intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

def merge(intervals):
    intervals.sort(key=lambda x:x[0])

    merged=[intervals[0]]

    for i in range(1,len(intervals)):
        if merged[-1][1]>=intervals[i][0]:
            merged[-1][1]=max(merged[-1][1],intervals[i][1])
        else:
            merged.append(intervals[i])

    return merged

print(merge(intervals))