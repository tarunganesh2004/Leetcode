# Asteroid Collision

asteroids=[5,10,-5]

def asteroidCollision(arr):
    stack=[]
    for a in arr:
        while stack and a<0 and stack[-1]>0:
            diff=a+stack[-1]
            if diff<0:
                stack.pop()
            elif diff>0:
                a=0
            else:
                a=0
                stack.pop()
        if a!=0:
            stack.append(a)
                    
    return stack

print(asteroidCollision(asteroids)) # [5,10]