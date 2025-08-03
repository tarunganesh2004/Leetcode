# Maximum Fruits Harvested After at Most K Steps LC 2106(Hard)

fruits = [[2,8],[6,3],[8,6]]
startPos = 5
k = 4

def maxTotalFruits(fruits,startPos,k):
    max_fruits,f=0,0
    start=0

    for end,[p,a] in enumerate(fruits):
        f+=a
        if p<start:
            continue 

        while start<=end and p-fruits[start][0]+min(abs(startPos-p),abs(startPos-fruits[start][0]))>k:
            f-=fruits[start][1]
            start+=1
        
        max_fruits=max(max_fruits,f)
    return max_fruits

print(maxTotalFruits(fruits,startPos,k))  