# Count prefix and suffix pairs I LC 3402

# isPrefixAndSuffix(str1, str2) returns true if str1 is both a 
# prefix and a suffix of str2, and false otherwise.
# Return an integer denoting the number of index pairs (i, j) such that i < j, and isPrefixAndSuffix(words[i], words[j]) is true.
words=["a","aba","ababa","aa"]

def isPrefixAndSuffixBrute(words): # O(n^2*m) where m is the length of the longest word
    count=0
    n=len(words)

    for i in range(n):
        for j in range(i+1,n):
            str1=words[i]
            str2=words[j]

            if len(str1)>len(str2):
                continue # skip

            if str2.startswith(str1) and str2.endswith(str1):
                count+=1

    return count

# Optimal approach is to use a trie
class TrieNode:
    def __init__(self):
        self.children={} # stores child nodes for (prefix, suffix) pairs
        self.possible_ends=0 # number of words that end at this node

class PrefixSuffixTrie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self, word):
        cur=self.root
        for i in range(len(word)):
            pr=word[i] # pr is the prefix
            su=word[len(word)-1-i]

            # if the (pr,su) pair is not in the children of the current node, then create a new node
            if (pr,su) not in cur.children:
                cur.children[(pr,su)]=TrieNode()

            # move to the child node 
            cur=cur.children[(pr,su)]

            # increment the number of words that end at this node
            cur.possible_ends+=1

    def search(self,word):
        cur=self.root
        for i in range(len(word)):
            pr=word[i]
            su=word[len(word)-1-i]

            if (pr,su) not in cur.children:
                return 0

            cur=cur.children[(pr,su)]

        return cur.possible_ends
    
class Solution:
    def countPrefixSuffixPairs(self,words):
        count=0
        trie=PrefixSuffixTrie()

        for word in words[::-1]:
            count+=trie.search(word)
            trie.insert(word)

        return count
print(isPrefixAndSuffixBrute(words)) # 4

sol=Solution()
print(sol.countPrefixSuffixPairs(words)) # 4