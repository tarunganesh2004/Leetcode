# Count Largest Group LC 1399

n=13

def countLargestGroup(n):
    map={}
    for i in range(1,n+1):
        s=sum([int(x) for x in str(i)])
        # print(s)
        if s in map:
            map[s]+=1
        else:
            map[s]=1
    maxValue=max(map.values())
    count=0
    for v in map.values():
        if v==maxValue:
            count+=1
    return count


print(countLargestGroup(n)) # Output: 4
