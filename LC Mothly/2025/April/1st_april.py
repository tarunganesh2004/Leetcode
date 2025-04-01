# Solving Questions With BrainPower LC 2140

questions = [[3, 2], [4, 3], [4, 4], [2, 5]]

def mostPoints(questions):
    from collections import defaultdict
    dp=defaultdict(int)
    max_score=0
    i=len(questions)-1
    while i>=0:
        point,brainpower=questions[i]
        dp[i]=max(max_score,point+dp[i+brainpower+1])
        max_score=max(max_score,dp[i])
        i-=1
    return max_score

print(mostPoints(questions))