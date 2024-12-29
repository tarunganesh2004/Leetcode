# Implement Prefix Tree LC 208

class Trie:

    def __init__(self):
        self.dict={}

    def insert(self,word):
        d=self.dict

        for c in word:
            if c not in d:
                d[c]={}
            d=d[c]
        
        d["."]="."

    def search(self,word):
        d=self.dict

        for c in word:
            if c not in d:
                return False
            d=d[c]
        
        return "." in d
    
    def startsWith(self,prefix):
        d=self.dict

        for c in prefix:
            if c not in d:
                return False
            d=d[c]
        
        return True
    

# Test Cases
trie=Trie()
trie.insert("apple")
print(trie.search("apple")) # True
print(trie.search("app")) # False
print(trie.startsWith("app")) # True
trie.insert("app")
print(trie.search("app")) # True
