# Maximum Number of Events That Can Be Attended II LC 1751

from bisect import bisect_right


events= [[1,2,4],[3,4,3],[2,3,1]]
k=2

def maxValue(events,k):
    # sort events by end time
    events.sort(key=lambda x: x[1])
    n= len(events)

    # Extract just the end times for binary search
    ends=[e[1] for e in events]

    # precompute previous non-overlapping event index for each event
    prev_idx=[]
    for i in range(n):
        s= events[i][0]
        # find the rightmost event that ends before the current event starts
        idx=bisect_right(ends, s-1) - 1
        prev_idx.append(idx)

    # dp[i][j]=max value using first i events and at most j picks
    dp=[[0]*(k+1) for _ in range(n+1)]
    
    for i in range(1,n+1):
        start,end,value= events[i-1]
        for j in range(1,k+1):
            # option 1: skip this event
            option1= dp[i-1][j]
            # option 2: take this event + best from previous non-overlapping events
            option2=dp[prev_idx[i-1]+1][j-1]+value 
            dp[i][j]=max(option1, option2)
    return dp[n][k]

print(maxValue(events,k))  # Output: 7