# Find the Number of Ways to place People II LC 3027(Hard)

points=[[1,1,],[2,2],[3,3]]

def numbeOfPairs(points):
    res=0
    points.sort(key=lambda p:(p[0],-p[1]))

    for i,(x1,y1) in enumerate(points):
        y=float('-inf')
        for (x2,y2) in points[i+1:]:
            if y1>=y2>y:
                res+=1
                y=y2

    return res 

print(numbeOfPairs(points))