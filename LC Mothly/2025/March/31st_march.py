# Put Marbles in Bags LC 2551(Hard)

from itertools import pairwise


weights=[1,3,5,1]
k=2

def putMarbles(weights,k):
    arr=sorted(map(sum,(pairwise(weights))))

    return sum(arr[len(arr)-k+1:])-sum(arr[:k-1])

print(putMarbles(weights,k))