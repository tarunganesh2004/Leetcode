# Removing Stars from a String LC 2390

s="leet**cod*e"

def removeStars(s):
    stack=[]
    n=len(s)
    for i in range(n):
        if s[i]=="*":
            if stack:
                stack.pop()
        else:
            stack.append(s[i])
    return "".join(stack)

print(removeStars(s))