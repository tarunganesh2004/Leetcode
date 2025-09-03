# Find the Number of Ways to Place People I LC 3025

points=[[1,1],[2,2],[3,3]]

def numberOfPairs(points):
    points.sort(key=lambda x:(-x[0],x[1]))

    n,ans=len(points),0
    for i in range(n-1):
        y=1<<31
        for j in range(i+1,n):
            if y>points[j][1]>=points[i][1]:
                ans+=1
                y=points[j][1]
    return ans

print(numberOfPairs(points))