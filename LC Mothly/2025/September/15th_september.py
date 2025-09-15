

text="hello world"
brokenLetters="ad"

def canBeTypedWords(text,brokenLetters):
    broken=set(brokenLetters)
    s=text.split()
    count=0
    for word in s:
        for char in word:
            if char in broken:
                break
        else:
            count+=1
    return count

print(canBeTypedWords(text,brokenLetters))