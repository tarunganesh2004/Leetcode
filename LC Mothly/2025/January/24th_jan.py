# # Find Eventual Safe States LC 802

# There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

# A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

# Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

graph=[[1,2],[2,3],[5],[0],[5],[],[]] # 0->1,2, 1->2,3, 2->5, 3->0, 4->5, 5->, 6->
# terminal nodes means nodes with no outgoing edges, so 5,6 are terminal nodes
# safe nodes are 2,4,5,6 as they lead to terminal nodes

# Approach is to use a dfs to find the safe nodes. We will use a visited array to keep track of the nodes visited in the current dfs. We will use a safe array to keep track of the safe nodes. If we encounter a node that is already visited in the current dfs, then we return False, as it is a cycle. If we encounter a node that is already visited in the previous dfs, then we return True, as it is a safe node. If we encounter a node that is not visited, then we recursively call the dfs on its neighbors. If all the neighbors are safe, then the current node is safe. If any of the neighbors are not safe, then the current node is not safe. We will return True if the current node is safe, else False.
def eventualSafeNodes(graph): # O(V+E) time complexity, O(V) space complexity
    def dfs(node):
        if visited[node]==1:
            return False
        if visited[node]==2:
            return True
        visited[node]=1
        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False
        visited[node]=2
        return True
    n=len(graph)
    visited=[0]*n
    safe=[]
    for i in range(n):
        if dfs(i):
            safe.append(i)
    return safe

print(eventualSafeNodes(graph)) # [2,4,5,6]