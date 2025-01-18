# Search Suggestions System LC 1268

# the approach is similar to the trie implementation
# but here we 
# 1) modify the trienode(instead of just storing children,store a list of atmost 3 words starting with the prefix)
# 2)Modify insert operation,As we insert each word, store it in the nodes along the path, maintaining only the top 3 lexicographically smallest words.
# 3) modify search operation for prefix suggestion, as we type each character move through the trie and collect suggestions at each node.

# Time complexity for insert and search is O(n) where n is the length of the word

class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.words=[] # stores at most 3 lexographically smallest words 

    def put(self,ch,node):
        self.children[ord(ch)-ord('a')]=node

    def get(self,ch):
        return self.children[ord(ch)-ord('a')]
    
    def contains_key(self,ch):
        return self.children[ord(ch)-ord('a')] is not None
    
    def add_word(self,word):
        # stores only top 3 lexographically smallest words
        if len(self.words)<3:
            self.words.append(word)

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        temp=self.root
        for ch in word:
            if not temp.contains_key(ch): # type: ignore
                temp.put(ch,TrieNode()) # type: ignore
            temp=temp.get(ch) # type: ignore
            temp.add_word(word) # type: ignore # store the word in the current node
        
    def get_suggestions(self,prefix):
        temp=self.root
        res=[]
        for ch in prefix:
            if not temp.contains_key(ch): # type: ignore
                break # if prefix is not found return empty list
            temp=temp.get(ch) # type: ignore
            # get top 3 words from the current prefix
            res.append(temp.words) # type: ignore

        # if prefix search stopped early, fill the remaining suggestions with empty list
        while len(res)<len(prefix):
            res.append([])

        return res
    
class Solution:
    def suggestedProducts(products,searchWord): # type: ignore
        products.sort() # type: ignore
        t=Trie()
        for product in products: # type: ignore
            t.insert(product)
        
        return t.get_suggestions(searchWord)
    
products=["mobile","mouse","moneypot","monitor","mousepad"]
searchWord="mouse"
print(Solution.suggestedProducts(products,searchWord)) # type: ignore # [["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]