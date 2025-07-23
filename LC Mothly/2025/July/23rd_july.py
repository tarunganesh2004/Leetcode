# Maximum Score From Removing Substrings LC 1717

s = "cdbcbbaaabab"
x = 4
y= 5

def maximumGain(s,x,y):
    def remove_substring(s,first,second,points):
        stack=[]
        score=0
        for ch in s:
            if stack and stack[-1] == first and ch == second:
                stack.pop()
                score += points
            else:
                stack.append(ch)
        return ''.join(stack), score
    
    if x > y:
        # remove ab first
        s, score1 = remove_substring(s, 'a', 'b', x)
        s,score2= remove_substring(s, 'b', 'a', y)
    else:
        # remove ba first
        s, score1 = remove_substring(s, 'b', 'a', y)
        s, score2 = remove_substring(s, 'a', 'b', x)
    return score1 + score2

print(maximumGain(s, x, y))  # Output: 19