# Find the Kth-Character in the String Game II LC 3307

k=5
operations=[0,0,0]

def kthCharacter(k, operations):
    cnt=0
    n=len(operations)
    length=pow(2,n-1)
    for i in range(n-1,-1,-1):
        if k>length:
            k-= length
            if operations[i] == 1:
                cnt += 1
        length //= 2
    return chr(ord('a')+(cnt%26))
    
print(kthCharacter(k, operations))  # Output: 'a'