# Count and Say LC 38

n=4

def countAndSay(n):
    if n == 1:
        return "1"
    else:
        prev = countAndSay(n - 1)
        result = ""
        count = 1
        for i in range(1, len(prev)):
            if prev[i] == prev[i - 1]:
                count += 1
            else:
                result += str(count) + prev[i - 1]
                count = 1
        result += str(count) + prev[-1]
        return result
    

print(countAndSay(n)) # Output: "1211"