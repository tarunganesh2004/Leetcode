# # Find the Number of Distinct Colors among the balls LC 3160

# You are given an integer limit and a 2D array queries of size n x 2.

# There are limit + 1 balls with distinct labels in the range [0, limit]. Initially, all balls are uncolored. For every query in queries that is of the form [x, y], you mark ball x with the color y. After each query, you need to find the number of distinct colors among the balls.

# Return an array result of length n, where result[i] denotes the number of distinct colors after ith query.

# Note that when answering a query, lack of a color will not be considered as a color.

from collections import defaultdict
limit=4
queries=[[1,4],[2,5],[1,3],[3,4]]

# brute force using map
def bruteForce(limit,queries): # O(n^2) & O(n)
    ans=[]
    colors={}
    for x,y in queries:
        colors[x]=y
        ans.append(len(set(colors.values())))

    return ans

# instead of computing len(set(colors.values())) every time, we can keep a count of colors and update it accordingly
def queryResults(limit,queries):
    color_map={}
    color_count=defaultdict(int) # stores occurence of each color
    unique_colors=set()
    ans=[]

    for x,y in queries:
        if x in color_map:
            old_color=color_map[x]
            color_count[old_color]-=1
            if color_count[old_color]==0:
                unique_colors.remove(old_color)

        # assign new color
        color_map[x]=y
        color_count[y]+=1
        unique_colors.add(y) # always add new color to unique_colors

        ans.append(len(unique_colors))

    return ans

# another approach using two maps one for ball to color and other for color count
def anotherWay(limit,queries):
    res=[]
    distinct=0
    ball_to_color={} # ball:color
    color_to_count={} # color:count of the color

    for ball,new_color in queries:
        if ball in ball_to_color:
            old_color=ball_to_color[ball]
            color_to_count[old_color]-=1
            if color_to_count[old_color]==0:
                # unique color is removed
                del color_to_count[old_color]
                distinct-=1

        # update the ball's color and color count
        ball_to_color[ball]=new_color
        if new_color in color_to_count:
            color_to_count[new_color]+=1
        else:
            # unique color is added
            color_to_count[new_color]=1
            distinct+=1

        res.append(distinct)

    return res


print(bruteForce(limit,queries))
print(queryResults(limit,queries))
print(anotherWay(limit,queries))