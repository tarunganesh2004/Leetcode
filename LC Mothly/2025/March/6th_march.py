# Find Missing and Repeated Values LC 2965

grid=[[1,3],[2,2]] # 1-n^2 values, 2 is repated and 4 is missing

def findMissingAndRepeated(grid):
    n=len(grid)
    freq={}
    for row in grid:
        for val in row:
            if val in freq:
                freq[val]+=1
            else:
                freq[val]=1
    
    for num in range(1,n*n+1):
        if num not in freq:
            missing=num
        elif freq[num]==2:
            repeated=num
    return [repeated,missing]

# using set
def anotherApproach(grid):
    n=len(grid)
    curSum=(n*n)*((n*n)+1)//2
    seen=set()
    for i in range(n):
        for j in range(n):
            if grid[i][j] not in seen:
                seen.add(grid[i][j])
                curSum-=grid[i][j]
            else:
                repeated=grid[i][j]
    return [repeated,curSum]

print(findMissingAndRepeated(grid))

print(anotherApproach(grid))