# Find the Kth-Character in the String Game II LC 3307

k=5
operations=[0,0,0]

def kthCharacter(k, operations):
    res=0
    k-=1
    for i,v in enumerate(operations):
        if k &(1<<i):
            res+=v
        return chr(ord('a')+res%26)
    
print(kthCharacter(k, operations))  # Output: 'a'