# 1497 Check if array Pairs are divisble by k 

l=[2,9,0,-4,-2,10]
l1=[3,8,17,2,5,6]
k=5

def canArrange(l,k):
    n=len(l)

    if n%2!=0:
        return False
    
    remainder_map={}

    for i in range(n):
        remainder=l[i]%k # -4%5 = 5-4=1, -2%5=5-2=3 , remainder map
        if remainder in remainder_map:
            remainder_map[remainder]+=1
        else:
            remainder_map[remainder]=1

    print(remainder_map) # {2: 1, 4: 1, 0: 2, 1: 1, 3: 1}

    for r,c in remainder_map.items():
        if r==0:
            if c%2!=0:
                return False
            
        elif 2*r==k:
            if c%2!=0:
                return False
        else:
            com=k-r
            if com not in remainder_map or remainder_map[com]!=c:
                return False
        
    return True
                
print(canArrange(l,k))
print(canArrange(l1,10)) # False