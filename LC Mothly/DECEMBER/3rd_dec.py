# Adding spaces to a string

s="LeetcodeHelpsMeLearn"
spaces=[8,13,15]

def addSpaces(s,spaces):
    res=[]

    first=0
    second=0

    while first<len(s):
        if second<len(spaces) and first==spaces[second]:
            res.append(" ")
            second+=1
        res.append(s[first])
        first+=1

    
    # for i in range(len(s)):

    #     if s[i]!=" ":
    #         res.append(s[i])
    #         first+=1
    #     for j in range(len(spaces)):
    #         if first==spaces[j] and second<len(spaces):
    #             res.append(" ")
    #             second+=1
        
    return "".join(res)

def anotherway(s,spaces):
    index,res=0,[]

    for space in spaces:
        res.append(s[index:space])
        index=space

    res.append(s[index:])
    return " ".join(res)

print(addSpaces(s,spaces))
print(anotherway(s,spaces))
        