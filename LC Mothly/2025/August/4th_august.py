# Fruits into Baskets LC 904

fruits=[1,2,1]

def totalFruits(fruits):
    from collections import defaultdict
    n=len(fruits)
    left=0
    max_len=0
    count=defaultdict(int)
    for right in range(n):
        count[fruits[right]]+=1

        while len(count)>2:
            count[fruits[left]]-=1
            if count[fruits[left]]==0:
                del count[fruits[left]]
            left+=1
        max_len=max(max_len,right-left+1)
    return max_len

print(totalFruits(fruits))  # Output: 3