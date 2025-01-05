# Shifting Letters II LC 2381

s="abc"
shifts=[[0,1,0],[1,2,1],[0,2,1]] # [start,end, direction], direction=0 means left shift, direction=1 means right shift
# output for first zac,next zbd next ace

def shiftingLetters(s,shifts):
    n=len(s)
    diff=[0]*(n+1)
    for shiftOp in shifts:
        start,end,direction=shiftOp
        diff[start]+=(1 if direction==1 else -1)
        if end+1<n:
            diff[end+1]-=(1 if direction==1 else -1)
            
    curShift=0
    shiftList=list(s)
    for i in range(n):
        curShift+=diff[i]
        newShift=(curShift%26+26)
        shiftList[i]=chr((ord(shiftList[i])-ord('a')+newShift)%26+ord('a'))

    return "".join(shiftList)

print(shiftingLetters(s,shifts))