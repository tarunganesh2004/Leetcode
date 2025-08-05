# Fruits into Baskets II LC 3477

fruits=[4,2,5]
baskets=[3,5,4]

def numOfUnplacedFruits(fruits,baskets):
    n=len(fruits)
    count=0

    for fruit in fruits:
        unset=1
        for i in range(n):
            if fruit<=baskets[i]:
                baskets[i]=0
                unset=0
                break
        count+=unset
    return count

print(numOfUnplacedFruits(fruits,baskets))  # Output: 1