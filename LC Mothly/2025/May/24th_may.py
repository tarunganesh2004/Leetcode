# Find words containing character

words=["leet","code"]
x="e"

def findWordsContainingChar(words, x):
    res=[]
    for i in range(len(words)):
        if x in words[i]:
            res.append(i)
    return res

print(findWordsContainingChar(words, x))  