# Rearranging Fruits LC 2561(Hard)

from collections import Counter


basket1=[4,2,2,2]
basket2=[1,4,1,2]

def minCost(basket1,basket2):
    count1=Counter(basket1)
    for num in basket2:
        count1[num]-=1
    
    last=[]
    for k,v in count1.items():
        # if freq is odd,split is not possible
        if v%2!=0:
            return -1
        last+=[k]*abs(v//2)

    minx=min(*basket1,*basket2)
    last.sort()

    return sum(min(2*minx,x) for x in last[:len(last)//2])

print(minCost(basket1,basket2))