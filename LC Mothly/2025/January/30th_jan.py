# # Divide Nodes into the Maximum Number of Groups LC 2493

# You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

# You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

# Divide the nodes of the graph into m groups (1-indexed) such that:

# Each node in the graph belongs to exactly one group.
# For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
# Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.


from collections import deque


n=6
edges=[[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]

class Solution:
    def magnificentSets(self,n,edges):
        adj_list=[[] for _ in range(n)]
        parent=[-1]*n
        depth=[0]*n

        for edge in edges:
            adj_list[edge[0]-1].append(edge[1]-1)
            adj_list[edge[1]-1].append(edge[0]-1)
            self._union(edge[0]-1,edge[1]-1,parent,depth)

        num_groups_for_component={}
        for node in range(n):
            num_groups=self.get_number_of_groups(adj_list,node,n)
            if num_groups==-1:
                return -1
            root=self._find(node,parent)
            num_groups_for_component[root]=max(num_groups_for_component.get(root,0),num_groups)
        return sum(num_groups_for_component.values())
    
    def get_number_of_groups(self,adjList,src_node,n):
        q=deque()
        seen=[-1]*n
        q.append(src_node)
        seen[src_node]=0
        deep_layer=0

        while q:
            size=len(q)
            for _ in range(size):
                cur_node=q.popleft()
                for nei in adjList[cur_node]:
                    if seen[nei]==-1:
                        seen[nei]=deep_layer+1
                        q.append(nei)
                    else:
                        if seen[nei]==deep_layer:
                            return -1
            deep_layer+=1
        return deep_layer
    
    def _find(self,node,parent):
        while parent[node]!=-1:
            node=parent[node]
        return node
    
    def _union(self,node1,node2,parent,depth):
        root1=self._find(node1,parent)
        root2=self._find(node2,parent)
        if root1==root2:
            return
        if depth[root1]>depth[root2]:
            parent[root2]=root1
        elif depth[root1]<depth[root2]:
            parent[root1]=root2
        else:
            parent[root2]=root1
            depth[root1]+=1

sol=Solution()
print(sol.magnificentSets(n,edges)) # 4