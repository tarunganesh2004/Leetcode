# Find the Original Typed String I LC 3330

word="abbcccc"

def possibleStringCount(word):
    n=len(word)
    v=set()
    i=0

    while i<n:
        cur=word[i]
        start=i 

        while i<n and word[i]==cur:
            i+=1
        
        length=i-start

        v.add(word)

        for red in range(1,length):
            r=word[:start]+cur*red+word[i:]
            v.add(r)

    return len(v)

print(possibleStringCount(word))  # Output: 5