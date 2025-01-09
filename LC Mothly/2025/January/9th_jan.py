# Counting words with a given prefix LC 2185

from collections import defaultdict


words = ["pay", "attention", "practice", "attend"]
pref="at"

# using builtin
def prefixCount(words,pref):
    count=0
    for word in words:
        if word.startswith(pref):
            count+=1
    return count

print(prefixCount(words,pref))

# Using Trie 
class TrieNode:
    def __init__(self):
        self.children=defaultdict()
        self.word_count=0
        
class Trie():
    def __init__(self):
        self.root=TrieNode()
        
    def insert(self,word):
        cur=self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch]=TrieNode()
            cur=cur.children[ch]
            cur.word_count+=1
            
    def count_word_with_prefix(self,pref):
        cur=self.root
        for ch in pref:
            if ch not in cur.children:
                return 0
            cur=cur.children[ch]
        return cur.word_count
    
class Solution:
    def countPrefix(self,words,pref):
        trie=Trie()
        for word in words:
            trie.insert(word)
        return trie.count_word_with_prefix(pref)
    
sol=Solution()
print(sol.countPrefix(words,pref)) # 2