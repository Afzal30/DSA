#https://leetcode.com/problems/prefix-and-suffix-search/description/

#approach 1 - using Trie
class WordFilter:

    def __init__(self, words):
        self.trie = {}

        for index, word in enumerate(words):
            length = len(word)

            # generate all suffixes
            for i in range(length + 1):
                key = word[i:] + "#" + word
                self._insert(key, index)

    def _insert(self, key, index):
        node = self.trie

        for ch in key:
            if ch not in node:
                node[ch] = {}
            node = node[ch]

            # store max index at every node
            node["$"] = index

    def f(self, pref, suff):
        node = self.trie
        key = suff + "#" + pref

        for ch in key:
            if ch not in node:
                return -1
            node = node[ch]

        return node.get("$", -1)


#approach 2 - straightforward using string method - interveiwer will accept for smaller inputs

class WordFilter:

    def __init__(self, words):
        self.words = words

    def f(self, pref, suff):
        for i in range(len(self.words)-1, -1, -1):
            w = self.words[i]
            if w.startswith(pref) and w.endswith(suff):
                return i
        return -1
