# Best Sightseeing pair LC 1014

values=[8,1,5,2,6]

def maxScoreSightseeingPair(values):
    # Brute force approach is to use two loops and find the max value
    res=0
    cur_max=values[0]-1 # here -1 is because when we add the second element the distance b/w them is 1
    for i in range(1,len(values)):
        res=max(res,values[i]+cur_max)
        cur_max=max(cur_max-1,values[i]-1)
    return res

def anotherApproach(values):
    current_best_first = values[0] - 1
    current_best = 0
    for i in range(1, len(values)):
        value = values[i]
        score = current_best_first + value
        if current_best < score:
            current_best = score
        if current_best_first < value:
            current_best_first = value
        current_best_first -= 1
    return current_best

print(maxScoreSightseeingPair(values))
print(anotherApproach(values))