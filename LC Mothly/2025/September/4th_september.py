# Find Closest Persion LC 3516

x=2
y=5
z=6

def findClosest(x,y,z):
    d1=abs(x-z)
    d2=abs(y-z)

    if d1<d2:
        return 1
    elif d2<d1:
        return 2
    else:
        return 0
    
print(findClosest(x,y,z))