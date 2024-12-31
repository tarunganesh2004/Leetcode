# Check if a word occurs as a prefix of any word in a sentence


sentence="i love eating burger"
searchWord="burg"

def isPrefixWord(sentence,searchWord):
    s=sentence.split()
    
    for i in range(len(s)):
        if s[i].startswith(searchWord):
            return i+1
    
    return -1

print(isPrefixWord(sentence,searchWord))