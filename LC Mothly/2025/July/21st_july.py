# Delete Characters to Make Fancy String LC 1957

s="leeetcode"

def makeFancyString(s):
    res=[]
    cnt=1
    prev=None 
    for c in s:
        if c==prev:
            cnt+=1
        else:
            cnt=1
        if cnt<3:
            res.append(c)
        prev=c
    return "".join(res)

print(makeFancyString(s))  # Output: "leetcode"