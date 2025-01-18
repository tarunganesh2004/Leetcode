# class TrieNode:
#     def __init__(self):
#         self.children=[None]*26
#         self.isEndOfWord=False

#     def put(self,ch,node):
#         self.children[ord(ch)-ord('a')]=node

#     def get(self,ch):
#         return self.children[ord(ch)-ord('a')]

#     def contains_key(self,ch):
#         return self.children[ord(ch)-ord('a')] is not None
    
#     def setEnd(self):
#         self.isEndOfWord=True
    

# class Trie:
#     def __init__(self):
#         self.root=TrieNode()

#     def insert(self,word):
#         temp=self.root
#         for ch in word:
#             if not temp.contains_key(ch): # type: ignore
#                 temp.put(ch,TrieNode()) # type: ignore
#             temp=temp.get(ch) # type: ignore
#         temp.setEnd() # type: ignore

#     def search(self,word):
#         temp=self.root
#         for ch in word:
#             if not temp.contains_key(ch): # type: ignore
#                 return False
#             temp=temp.get(ch) # type: ignore
#         return temp.isEndOfWord # type: ignore
    
#     def startsWith(self,prefix):
#         temp=self.root
#         for ch in prefix:
#             if not temp.contains_key(ch): # type: ignore
#                 return False 
#             temp=temp.get(ch) # type: ignore
#         return True
    
# t=Trie()
# t.insert("apple")
# print(t.search("apple")) # True
# print(t.search("app")) # False
# print(t.startsWith("app")) # True
# t.insert("app")
# print(t.search("app")) # True

# Another way to implement Trie is to use dictionary

class Trie:
    def __init__(self):
        self.dic={}

    def insert(self,word):
        d=self.dic
        for ch in word:
            if ch not in d:
                d[ch]={}
            d=d[ch]
        d["."]="." # end of word

    def search(self,word):
        d=self.dic
        for ch in word:
            if ch not in d:
                return False
            d=d[ch]
        return "." in d
    
    def startsWith(self,prefix):
        d=self.dic
        for ch in prefix:
            if ch not in d:
                return False
            d=d[ch]
        return True
    
t=Trie()
t.insert("apple")
print(t.search("apple")) # True
print(t.search("app")) # False
print(t.startsWith("app")) # True
t.insert("app")
print(t.search("app")) # True