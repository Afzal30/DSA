#https://leetcode.com/problems/kth-ancestor-of-a-tree-node/



class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.anc = [ [ parent[i] for i in range(n) ] ]
        #print(self.anc)
        for i in range(1,16):
            self.anc.append([])
            #print(self.anc)
            for v in range(n):
                if self.anc[i-1][v] == -1:
                    self.anc[i].append(-1)
                else:
                    self.anc[i].append( self.anc[i-1][self.anc[i-1][v]])
        #print("xxxxxxxxxxxxxxxxxxxxxxxx")           
        #print(self.anc)

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(16):
            if node == -1:
                return -1
            if (1 << i) & k :
                node = self.anc[i][node]

        return node
        

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
