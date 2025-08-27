# Length of Longest V-Shaped Diagonal Segment LC 3459


grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]


def lenOfVDiagonal(grid):
    m,n=len(grid),len(grid[0])
    directions=[(1,1),(1,-1),(-1,-1),(-1,1)]
    memo={}
    def dfs(r,c,d,hasTurned,need2):
        tup=(r,c,d,hasTurned,need2)
        if tup in memo:
            return memo[tup]
        
        new_r,new_c=r+directions[d][0],c+directions[d][1]
        expected= 2 if need2 else 0

        if 0<=new_r<m and 0<=new_c<n and grid[new_r][new_c]==expected:
            best=dfs(new_r,new_c,d,hasTurned,not need2)
            if not hasTurned:
                new_d=(d+1)%len(directions)
                best=max(best,dfs(new_r,new_c,new_d,True,not need2))
            memo[tup]=best+1
            return best+1
        else:
            memo[tup]=0
            return 0
    
    ans=0
    for i in range(m):
        for j in range(n):
            if grid[i][j]==1:
                for d in range(len(directions)):
                    ans=max(ans,1+dfs(i,j,d,False,2))
    return ans 

print(lenOfVDiagonal(grid))