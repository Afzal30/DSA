#https://leetcode.com/problems/implement-trie-prefix-tree/description/

#using TrieNode
class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_End = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:

        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.is_End = True
        

    def search(self, word: str) -> bool:

        node = self.root

        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]

        return node.is_End
        

    def startsWith(self, prefix: str) -> bool:

        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


#Using just python dictionary

class Trie:

    def __init__(self):
        self.emptyDictionary = {}

    def insert(self, word: str) -> None:
        #reference to my empty Dictionary
        newword = self. emptyDictionary
        for eachChar in word:
            if eachChar not in newword:
                newword[eachChar] = {}
            newword = newword[eachChar] 
        newword['.'] = "End of Word" 

    def search(self, word: str) -> bool:
        newword = self.emptyDictionary
        for eachChar in word:
            if eachChar not in newword:
                return False
            newword = newword[eachChar]
        if '.' in newword:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        newword = self.emptyDictionary
        for eachChar in prefix:
            if eachChar not in newword:
                return False
            newword = newword[eachChar]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
