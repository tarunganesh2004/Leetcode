# Divide a String into Groups of Size K LC 2138

s="abcdefghi"
k=3
fill='x'

def divideString(s, k, fill):
    n = len(s)
    result = []
    
    for i in range(0, n, k):
        part = s[i:i+k]
        if len(part) < k:
            part += fill * (k - len(part))
        result.append(part)
    
    return result

print(divideString(s, k, fill))  # Output: ['abc', 'def', 'ghi', 'xxx']