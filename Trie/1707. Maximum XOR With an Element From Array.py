#https://leetcode.com/problems/maximum-xor-with-an-element-from-array/

class Trie:
    def __init__(self):
        self.tree = {}   
        self.bits = 31
    
    # adds binary representation of a number to trie
    def add(self,value):
        node = self.tree
        for i in range(self.bits,-1,-1):
            bit = 1 if (1<<i) & value else 0
            if bit not in node : node[bit] = {}
            node = node[bit]
        return 

    # finda max Xor of 'value' with every number present in trie
    def findMax(self,value):
        if not self.tree : return -1   
        node = self.tree
        maxXor = 0
        for i in range(self.bits,-1,-1):
            bit = 1 if (1<<i) & value else 0
            req = 1-bit
            if req in node:
                maxXor |= (1<<i)
                node = node[req]
            else:
                node = node[bit]
        return maxXor



class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        n = len(nums)
        trie = Trie()

        nums.sort()

        queries = [ [i[0],i[1],ind] for ind,i in enumerate(queries)]
        queries.sort(key = lambda x : x[1])

        res = [-1] * len(queries)

        index = 0

        for x,maxvalue,i in queries:
            while index<n and nums[index] <=maxvalue:
                trie.add(nums[index])
                index += 1

            res[i] = trie.findMax(x)

        return res
        
