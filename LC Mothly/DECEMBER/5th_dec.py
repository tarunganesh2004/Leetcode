# Move pieces to obtain a String LC 2337

start="_L__R__R_"
target="L______RR"

def canChange(start,target):
    if len(start)!=len(target) or start.replace('_','')!=target.replace('_',''):
        return False
    
    n=len(start)
    # using two pointers
    i=j=0

    while i<n and j<n:
        while i<n and start[i]=='_':
            i+=1
        while j<n and target[j]=='_':
            j+=1
        
        if i<n and j<n and (start[i]=='L' and i<j or start[i]=='R' and i>j):
            return False
        i+=1
        j+=1
    return True

print(canChange(start,target))