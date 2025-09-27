# Largest Triangle Area LC 812

points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
def area(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0)

def largestTriangleArea(points):
    max_area = 0
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                x3, y3 = points[k]
                current_area = area(x1, y1, x2, y2, x3, y3)
                max_area = max(max_area, current_area)
    return max_area

print(largestTriangleArea(points))