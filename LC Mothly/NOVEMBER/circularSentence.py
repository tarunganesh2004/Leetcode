s="leetcode exercises sound delightful"
s1="eetcode"

def circularSentence(s):
    n=len(s)
    if n==1:
        return s[0]==s[-1]
    l=s.split(" ")

    for i in range(len(l)):
        temp=l[i]
        temp1=l[i+1] if i+1<len(l) else l[0]

        if temp[-1]!=temp1[0]:
            return False
        
    return True

print(circularSentence(s))
print(circularSentence(s1))