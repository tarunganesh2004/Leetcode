# Find the Lexicographically Largest String From the Box I LC 3403

word="dbca"
numFriends=2

def lastSubstring(s):
    i,j,n=0,1,len(s)
    while j<n:
        k=0
        while j+k<n and s[i+k]==s[j+k]:
            k+=1
        if j+k<n and s[i+k]<s[j+k]:
            i,j=j,max(j+1,i+k+1)
        else:
            j=j+k+1
    return s[i:]

def answerString(word,numFriends):
    if numFriends == 1:
        return word
    last=lastSubstring(word)
    n,m=len(word),len(last)
    return last[:min(m,n-numFriends+1)]


print(answerString(word, numFriends))  # Output: "dbc"