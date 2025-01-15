# Asteroid Collision LC 735

arr=[5,10,-5]
arr1=[10,2,-5]

def asteroidCollision(arr):
    stack=[]
    for a in arr:
        print(a,stack)
        while stack and a<0 and stack[-1]>0:
            print(a,stack[-1])
            dif=a+stack[-1]
            print(dif)
            if dif<0:
                print(stack)
                stack.pop()
            elif dif>0:
                print(stack)
                a=0
            else:
                a=0
                stack.pop()
            print(stack)
        if a!=0:
            print(stack)
            stack.append(a)
    return stack

print(asteroidCollision(arr1))