# Most Profitable Path in a Tree LC 2467

from collections import defaultdict, deque


edges=[[0,1],[1,2],[1,3],[1,4]]
bob=3
amount=[-2,4,2,-4,6]

# approach is to use bfs on alice , and dfs from bob, and keep a time variable to keep track of visited nodes by bob, and then calculate the profit

def mostProfitablePath(edges,bob,amount):
    adj=defaultdict(list)
    for v1,v2 in edges:
        adj[v1].append(v2)
        adj[v2].append(v1)

    # dfs for bob simulation
    bob_times={} # node on root path -> time visited
    def dfs(src,prev_node,time):
        if src==0:
            bob_times[src]=time
            return True
        for nei in adj[src]:
            if nei==prev_node:
                continue
            if dfs(nei,src,time+1):
                bob_times[src]=time
                return True
        return False
    dfs(bob,-1,0)

    # bfs for alice simulation
    q=deque([(0,0,-1,amount[0])]) #(node,time,prev_node,total Profit)
    res=float('-inf')
    while q:
        node,time,prev_node,profit=q.popleft()
        for nei in adj[node]:
            if nei==prev_node:
                continue
            nei_profit=amount[nei]
            nei_time=time+1
            if nei in bob_times:
                if nei_time>bob_times[nei]:
                    nei_profit=0
                if nei_time==bob_times[nei]:
                    nei_profit=nei_profit//2
            
            q.append((nei,nei_time,node,profit+nei_profit))

            if len(adj[nei])==1: # consider total profit for leaf node 
                res=max(res,profit+nei_profit)

        
    return res

print(mostProfitablePath(edges,bob,amount)) # 6