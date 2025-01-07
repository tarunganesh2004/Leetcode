# String Matching in an Array LC 1408

words=["mass","as","hero","superhero"]

def stringMatchingBrute(words): # O(m^2*n^2) where m is the length of the longest word and n is the number of words
    # brute force 
    res=[]
    n=len(words)
    for cur_word_idx in range(n):
        for other_word_idx in range(n):
            if cur_word_idx!=other_word_idx and words[cur_word_idx] in words[other_word_idx]:
                res.append(words[cur_word_idx])
                break
    return res

def stringMatchingAnother(words):
    # another approach
    words.sort(key=len) 
    res=[]
    n=len(words)
    for i in range(n):
        for j in range(i+1,n):
            if words[i] in words[j]:
                res.append(words[i])
                break
    return res

print(stringMatchingBrute(words)) # ['as', 'hero']
print(stringMatchingAnother(words)) # ['as', 'hero']