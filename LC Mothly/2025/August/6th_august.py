# Fruits Into Baskets III LC 3479

from math import sqrt


fruits=[4, 2, 5]
baskets=[3, 5, 4]

def numOfUnplacedFruits(fruits, baskets):
    n,m=len(baskets),int(sqrt(len(baskets)))

    block=[max(baskets[i:i+m]) for i in range(0, n, m)]
    res=0

    for fruit in fruits:
        for b in range(len(block)):
            if block[b]>=fruit:
                for i in range(b*m, min((b+1)*m, n)):
                    if baskets[i]>=fruit:
                        baskets[i]=0
                        break 
                block[b]=max(baskets[b*m:(b+1)*m])
                break
        else:
            res+=1
    return res

print(numOfUnplacedFruits(fruits, baskets))  # Output: 1