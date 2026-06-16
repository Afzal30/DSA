#

#Approach 1 : Sort + Binary Search
"""
Sort A
For each prefix, do binary search
Get 3 words from the index and check if it matches the prefix
"""
class TrieNode():
    def __init__(self):
        self.children = {}
        self.end = False
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        #print(products)
        ans = []
        cur = ""
        for ch in searchWord:
            cur += ch
            #print("cur",cur)
            i = bisect.bisect_left(products,cur)
            #print(i)
            #print(products[i:i+3])
            ans.append( [w for w in products[i:i+3] if w.startswith(cur)] )
            print(ans)

        return ans


#Approach 2 : Trie

"""
Add word to trie while maintain a list of words of length 3 for each prefix
Search each prefix and return
"""

class TrieNode():
    def __init__(self):
        self.children = {}
        self.words = list()
        self.n = 0


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            if node.n < 3:
                node.words.append(word)
                node.n += 1

    def find_word_by_prefix(self,prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return []

            node = node.children[c]

        return node.words
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        for word in products:
            trie.insert(word)

        ans = []
        cur = ""

        for ch in searchWord:
            cur += ch
            ans.append(trie.find_word_by_prefix(cur))

        return ans
