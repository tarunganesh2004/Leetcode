# Minimum Number of Operations to Move All Balls to Each Box LC 1769

boxes="110" # [1,1,3]

def bruteForce(boxes):
    n=len(boxes)
    ans=[0]*n
    for i in range(n):
        for j in range(n):
            if boxes[j]=='1':
                ans[i]+=abs(j-i)
    return ans

def minOperations(boxes):
    n=len(boxes)
    ans=[0]*n
    # use prefix sum and suffix to calculate the number of balls to the left and right of each box
    # left to right prefix sum
    balls=0
    operations=0
    for i in range(n):
        ans[i]+=operations
        balls+=int(boxes[i])
        operations+=balls

    # right to left suffix sum
    balls=0
    operations=0
    for i in range(n-1,-1,-1):
        ans[i]+=operations
        balls+=int(boxes[i])
        operations+=balls

    return ans

print(bruteForce(boxes)) 

print(minOperations(boxes)) # [1,1,3]