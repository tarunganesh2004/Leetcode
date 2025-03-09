# Alternating Groups II LC 3208

colors=[0,1,0,1,0]
k=3

def numberOfAlternatingGroups(colors,k):
    colors.extend(colors[:(k-1)])
    count=0
    left=0
    for right in range(1,len(colors)):
        if right>0 and  colors[right]==colors[right-1]:
            left=right
        if right-left+1>=k:
            count+=1
        
    return count

print(numberOfAlternatingGroups(colors,k)) 