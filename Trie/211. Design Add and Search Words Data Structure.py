#https://leetcode.com/problems/design-add-and-search-words-data-structure/
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

        

    def addWord(self, word: str) -> None:
        cur_node = self.root
        for ch in word:
            cur_node = cur_node.children.setdefault(ch,TrieNode())

        cur_node.is_word = True
        

    def search(self, word: str) -> bool:

        def dfs(node, index):
            if index == len(word):
                return node.is_word

            if word[index]==".":
                for child in node.children.values():
                    if dfs(child,index+1):
                        return True

            if word[index] in node.children:
                return dfs(node.children[word[index]], index+1)

            return False

        return dfs(self.root,0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
