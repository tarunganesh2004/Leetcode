# Longest Binary Sequence Less than or Equal to K LC 2311

s="1001010"
k=5

def longestSubsequence(s,k):
    n=len(s)
    zeroes=s.count("0")
    ones=0
    value=0
    power=1

    
    for i in range(n-1,-1,-1):
        if s[i]=="1":
            if value+power>k:
                continue 
            value+=power
            ones+=1
        power<<=1
        if power>k:
            break
    
    return zeroes+ones

print(longestSubsequence(s,k))  