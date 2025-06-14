# Maximum Difference By Remapping a Digit LC 2566

num=11891

def minMaxDifference(num):
    s= str(num)
    t=s
    pos=0
    while pos<len(s) and s[pos]=="9":
        pos+=1
    if pos<len(s):
        s=s.replace(s[pos], "9")
    
    t=t.replace(t[0], "0")
    return int(s) - int(t)

print(minMaxDifference(num))  # Output: 99009