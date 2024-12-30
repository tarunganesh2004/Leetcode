# Max points on a line LC 149

# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
from math import gcd
points=[[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
#points=[[1,1],[2,2],[3,3]]

# bruteforce approach is to take all subsets and in each subset count the number of points that have same slope
# and then return the max of all the subsets O(2^n)

# A better approach is to use a hashmap to store the slope of the line formed by each pair of points
# and then count the number of points that have the same slope

def maxPoints(points):
    slopes={}
    n=len(points)
    if n==1:
        return 1
    max_points=0
    for i in range(n):
        for j in range(i+1,n):
            if points[i]==points[j]:
                continue
            if points[i][0]==points[j][0]:
                slope=float('inf')
            else:
                slope=(points[j][1]-points[i][1])/(points[j][0]-points[i][0])
            if slope not in slopes:
                slopes[slope]=set()
            slopes[slope].add(i)
            slopes[slope].add(j)
    for slope in slopes:
        max_points=max(max_points,len(slopes[slope]))
    return max_points

print(maxPoints(points))