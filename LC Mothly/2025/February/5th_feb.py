# Check if one string swap can make two strings equal LC 1790

s1="bank"
s2="kanb"

def areAlmostEqual(s1,s2):
    if s1==s2:
        return True
    if len(s1)!=len(s2):
        return False
    dif=[]
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            dif.append(i)
    if len(dif)!=2:
        return False
    return s1[dif[0]]==s2[dif[1]] and s1[dif[1]]==s2[dif[0]]

def otherApproach(s1,s2): # O(1) space
    if s1==s2:
        return True
    if sorted(s1)!=sorted(s2):
        return False
    count=0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            count+=1

    if count!=2:
        return False
    return True

print(areAlmostEqual(s1,s2))