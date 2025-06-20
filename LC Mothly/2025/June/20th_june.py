# Maximum Manhattan Distance After K Changes LC 3443

s="NWSE"
k=1

def maxDistance(s,k):
    def count(d1,d2,t):
        return abs(d1-d2) + 2 * t
    ans=0
    north=south=east=west=0
    for i in s:
        if i=='N':
            north+=1
        elif i=='S':
            south+=1
        elif i=='E':
            east+=1
        elif i=='W':
            west+=1
        t1=min(north,south,k)
        t2=min(east,west,k-t1)

        ans=max(ans,count(north,south,t1)+count(east,west,t2))
    return ans

print(maxDistance(s,k))  