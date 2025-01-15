# Celebrity Problem LC 277

def findCelebrity(arr):
    stack=[]
    for i in range(len(arr)):
        stack.append(i) # append all the people to the stack

    while len(stack)>=2:
        i=stack.pop()
        j=stack.pop()
        if arr[i][j]==1:
            stack.append(j)
        else:
            stack.append(i)

    potential_celebrity=stack.pop()
    for i in range(len(arr)):
        if i!=potential_celebrity:
            if arr[i][potential_celebrity]==0 or arr[potential_celebrity][i]==1:
                return -1
    return potential_celebrity

arr=[[0,1,0],[0,0,0],[0,1,0]]
print(findCelebrity(arr)) # 1