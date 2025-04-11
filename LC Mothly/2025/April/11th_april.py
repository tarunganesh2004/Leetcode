# Count Symmetric Integers LC 2843

low=1
high=100

def countSymmetricIntegers(low, high):
    def isSymmetric(x):
        s=str(x)
        n=len(s)
        if n%2!=0:
            return False
        left=s[:n//2]
        right=s[n//2:]
        return sum(map(int,left))==sum(map(int,right))
    
    cnt=0
    for i in range(low,high+1):
        if isSymmetric(i):
            cnt+=1
    return cnt

print(countSymmetricIntegers(low,high))