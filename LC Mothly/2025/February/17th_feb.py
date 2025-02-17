# # Letter Tile Possibilities LC 1079

# You have n  tiles, where each tile has one letter tiles[i] printed on it.

# Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

tiles="AAB"

def numTilePossibilities(tiles):
    res=set()
    def backtrack(path,tiles):
        if path:
            res.add(path)
        for i in range(len(tiles)):
            backtrack(path+tiles[i],tiles[:i]+tiles[i+1:])
    backtrack("",tiles)
    return len(res)

def optimizedWay(tiles):
    arr=list(tiles)
    arr.sort()
    vis=[False]*len(arr)
    c=0
    def dfs(arr,length,vis):
        if length==len(arr):
            return
        
        for i in range(len(arr)):
            if vis[i] or (i>0 and arr[i]==arr[i-1] and not vis[i-1]):
                continue
            vis[i]=True
            nonlocal c
            c+=1
            dfs(arr,length+1,vis)
            vis[i]=False

    dfs(arr,0,vis)
    return c

print(numTilePossibilities(tiles))
print(optimizedWay(tiles))