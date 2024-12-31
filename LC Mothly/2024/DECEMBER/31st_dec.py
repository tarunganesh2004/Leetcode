# LC 983 Minimum Cost For Tickets

days = [1,4,6,7,8,20]
costs = [2,7,15]

def mincostTickets(days,costs):
    travel_days=set(days)

    dp=[0]*366 # dp[i] is the minimum cost to travel upto day i
    for i in range(1,366):
        if i not in travel_days:
            dp[i]=dp[i-1]
        else:
            dp[i]=min(dp[i-1]+costs[0],dp[max(0,i-7)]+costs[1],dp[max(0,i-30)]+costs[2])
    return dp[365]

print(mincostTickets(days,costs))