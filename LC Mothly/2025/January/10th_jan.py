# Word Subsets LC 916
from collections import Counter


words1=["amazon","apple","facebook","google","leetcode"]
words2=["e","o"]
# Output: ["facebook","google","leetcode"]

def wordSubsets(words1,words2): # TC O(len(words2)+len(words1)*unique characters in words2)
    # build max frequency of each character in words2
    max_freq=Counter()
    for word in words2:
        word_count=Counter(word) 
        print(word_count)
        for ch in word_count:
            max_freq[ch]=max(max_freq[ch],word_count[ch])
    print("max_freq",max_freq)

    res=[]
    for word in words1:
        word_count=Counter(word)
        print(word_count)
        for ch in max_freq:
            if word_count[ch]<max_freq[ch]:
                break
        else:
            res.append(word)
    return res

print(wordSubsets(words1,words2)) # ["facebook","google","leetcode"]