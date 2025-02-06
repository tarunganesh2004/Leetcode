# Length of Last word

s="Hello World"

def lengthOfLastWord(s):
    w=s.split()
    if len(w)==0:
        return 0
    return len(w[-1])

print(lengthOfLastWord(s))