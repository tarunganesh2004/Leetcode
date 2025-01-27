# Course Schedule - IV LC 1462

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.

# For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
# Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c.

# You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.

# Return a boolean array answer, where answer[j] is the answer to the jth query.

numCourses=2
prerequisites=[[1,0]]
queries=[[0,1],[1,0]]

# brute force: for each query, check if there is a path from u to v
def checkIfPrerequisiteBrute(numCourses,prerequisites,queries): # TLE
    graph=[[] for _ in range(numCourses)]
    for a,b in prerequisites:
        graph[a].append(b)
    
    def dfs(u,v):
        if u==v:
            return True
        for nei in graph[u]:
            if dfs(nei,v):
                return True
        return False
    
    res=[]
    for u,v in queries:
        res.append(dfs(u,v))
    return res

# optimized way is to use Floyd-Warshall algorithm
# O(n^3) time and O(n^2) space
def checkIfPrerequisite(numCourses,prerequisites,queries):
    graph=[[False]*numCourses for _ in range(numCourses)]
    for a,b in prerequisites:
        graph[a][b]=True
    
    for k in range(numCourses):
        for i in range(numCourses):
            for j in range(numCourses):
                graph[i][j]|=(graph[i][k] and graph[k][j])
    
    res=[]
    for u,v in queries:
        res.append(graph[u][v])
    return res

# Another better approach
def anotherApproach(numCourses,prerequisites,queries):
    from collections import defaultdict
    graph=defaultdict(list)
    for prereq,postreq in prerequisites:
        graph[prereq].append(postreq)

    # for each course, find all the courses that can be taken after it
    # and store them in a set
    postreq_set=[set() for _ in range(numCourses)]

    def dfs(course):
        for postreq in graph[course]:
            if postreq not in postreq_set[course]:
                postreq_set[course].add(postreq)
                postreq_set[course].update(dfs(postreq))
        return postreq_set[course]
    
    for course in range(numCourses):
        dfs(course)

    res=[]
    for prereq,postreq in queries:
        res.append(postreq in postreq_set[prereq])
    return res
    

print(checkIfPrerequisiteBrute(numCourses,prerequisites,queries))
print(checkIfPrerequisite(numCourses,prerequisites,queries))
print(anotherApproach(numCourses,prerequisites,queries))