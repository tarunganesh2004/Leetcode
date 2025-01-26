# # Maximum Employees to be invited to a Meeting LC 2127

# # A company is organizing a meeting and has a list of n employees, waiting to be invited. They have arranged for a large circular table, capable of seating any number of employees.

# The employees are numbered from 0 to n - 1. Each employee has a favorite person and they will attend the meeting only if they can sit next to their favorite person at the table. The favorite person of an employee is not themself.

# Given a 0-indexed integer array favorite, where favorite[i] denotes the favorite person of the ith employee, return the maximum number of employees that can be invited to the meeting.

# example f=[2,2,1,2]
# Each employee's favorite:
# Employee 0 → 2
# Employee 1 → 2
# Employee 2 → 1
# Employee 3 → 2
# 0 → 2 ← 1
#     ↑
#     3
# Employees 0, 1, and 3 all want to sit next to 2.
# 2 wants to sit next to 1.
# We must seat employees in a circular manner while ensuring that everyone is next to their favorite.
# so a valid arrangement is 0->1->2 (back to 0)
# so the answer is 3
# we cant include employee 3 because 
# 3 also wants to sit next to 2, but 2 already has 0 and 1 next to them.
# 2 cannot be next to 1, 0, and 3 at the same time.
# So, we can only include 3 employees.
# 1->2->3 (back to 1) is also a valid arrangement. 
# So, the answer is 3.

from collections import deque


favorite=[2,2,1,2]

# the idea is to find the cycles and bidirectional pairs(2-cycles)
# we can build a graph where each employee is a node and each employee has a directed edge to their favorite person

def maxInvitations(favorite): # O(n) time and space
    n=len(favorite)

    # build the graph and store indegree values(number of times each employee is someone's favorite)
    graph=[[] for _ in range(n)]
    indegree=[0]*n 

    for i,fav in enumerate(favorite):
        graph[i].append(fav) # i->fav
        indegree[fav]+=1

    # now identify smallest chains(starting from leaves)
    # using topo sort
    queue=deque()
    for i in range(n):
        if indegree[i]==0: # if no one likes this person, they must be removed first
            queue.append(i)

    longest_chain=[1]*n # stores the longest chain ending at each node
    while queue:
        node=queue.popleft()
        fav=favorite[node]

        # extend the chain
        longest_chain[fav]=max(longest_chain[fav],longest_chain[node]+1)

        # reduce indegree and add to queue if indegree becomes 0
        indegree[fav]-=1
        if indegree[fav]==0:
            queue.append(fav)

    # detect and process cycles
    visited=[False]*n
    max_cycle_size=0
    sum_of_2_cycles=0

    for i in range(n):
        if indegree[i]>0: # means a cycle is present
            cycle_len=0
            node=i

            # count cycle length
            while not visited[node]:
                visited[node]=True
                node=favorite[node]
                cycle_len+=1

            if cycle_len==2: # bidirectional pair
                a,b=i,favorite[i]
                sum_of_2_cycles+=longest_chain[a]+longest_chain[b]
            else:
                max_cycle_size=max(max_cycle_size,cycle_len)

    return max(max_cycle_size,sum_of_2_cycles)

print(maxInvitations(favorite)) # 3
