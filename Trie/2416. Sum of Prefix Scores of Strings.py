#https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/
class TrieNode():
    def __init__(self):
        self.children = {}
        self.cp = 0


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self,value):
        node = self.root
        for ele in value:
            if ele not in node.children:
                node.children[ele] = TrieNode()
            node = node.children[ele]
            node.cp += 1


    def count_prefix(self,word):
        node = self.root
        tot_prefix = 0
        for ele in word:
            node = node.children[ele]
            tot_prefix += node.cp

        return tot_prefix


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        trie = Trie()
        for word in words:
            trie.insert(word)


        ans = []

        for word in words:
            ans.append(trie.count_prefix(word))
        
        return ans

        
        
