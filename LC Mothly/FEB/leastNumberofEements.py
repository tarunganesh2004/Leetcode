def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
    mp = {}
    for x in arr:
        mp[x] = mp.get(x, 0) + 1

    elements = sorted(mp.items(), key=lambda x: x[1])

    for key, value in elements:
        if value <= k:
            k -= value
            del mp[key]
        else:
            break
    return len(mp)


l=[4,3,1,1,3,3,2]
k=3
r=findLeastNumOfUniqueInts(l,k)
print(r)

