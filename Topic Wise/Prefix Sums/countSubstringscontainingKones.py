# Count of substrings containing K ones

s="10010"
k=1

def countSubstrings(s,k):
    map={0:1}
    ones_count=0
    count=0

    for char in s:
        if char=="1":
            ones_count+=1
        
        if ones_count-k in map:
            count+=map[ones_count-k]

        if ones_count in map:
            map[ones_count]+=1
        else:
            map[ones_count]=1
    
    return count

print(countSubstrings(s,k)) # 9