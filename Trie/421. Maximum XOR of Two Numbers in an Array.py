#https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/
#
class TrieNode:
    def __init__(self):
        self.links = [None,None] #size is 2, either 0 or 1 will be stored
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,num):
        node = self.root

        for i in range(31,-1,-1):
            bit = (num >> i) & 1

            if node.links[bit] is None:
                node.links[bit] = TrieNode()

            node = node.links[bit]



    def get_max_xor(self,num):
        node = self.root
        ans = 0

        for i in range(31,-1,-1):
            bit = (num >> i) & 1

            opposite = 1 - bit

            if node.links[opposite]:
                ans |= (1<<i)
                node = node.links[opposite]

            else:

                node = node.links[bit]

        return ans




class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()

        for num in nums:
            trie.insert(num)

        res = 0

        for num in nums:
            res = max(res,trie.get_max_xor(num))


        return res

        
