# Max points on a line LC 149

# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
from collections import defaultdict
from math import gcd
points=[[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
#points=[[1,1],[2,2],[3,3]]

# bruteforce approach is to take all subsets and in each subset count the number of points that have same slope
# and then return the max of all the subsets O(2^n)

# A better approach is to use a hashmap to store the slope of the line formed by each pair of points
# and then count the number of points that have the same slope

def maxPoints(points):
    mx=0
    if len(points)<=2:
        return len(points)
    
    for i in range(len(points)-1):
        m=[]
        for j in range(i+1,len(points)):
            dx=points[j][0]-points[i][0]
            dy=points[j][1]-points[i][1]

            if dx==0:
                dy='undef'
                m.append(dy)
            else:
                m.append(dy/dx)
        mx=max(mx,m.count(max(set(m),key=m.count))+1)
    return mx

def anotherApproachSimple(points):
    points.sort()
    slope,M=defaultdict(int),0
    for i,(x1,y1) in enumerate(points):
        slope.clear()
        for x2,y2 in points[i+1:]:
            dx,dy=x2-x1,y2-y1
            g=gcd(dx,dy)
            m=(dx//g,dy//g) if g else (dx,dy)
            slope[m]+=1
            M=max(M,slope[m])
    return M+1

print(maxPoints(points))
print(anotherApproachSimple(points))