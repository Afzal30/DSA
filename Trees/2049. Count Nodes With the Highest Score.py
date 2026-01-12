#https://leetcode.com/problems/count-nodes-with-the-highest-score/description/

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:

        children = {}
        n=len(parents)
        for i,e in enumerate(parents):
            if e in children:
                children[e].append(i)
            else:
                children[e]=[i]
        d= {}
        
        def count_nodes(node):
            product = 1
            summ = 0
            if node in children:
                for child in children[node]:
                    res = count_nodes(child)
                    product *= res
                    summ += res

            product *= max(1,n-1-summ)

            if product in d:
                d[product] += 1
            else:
                d[product] = 1

            return summ + 1

        count_nodes(0)

        print(d.keys())
        return d[max(d.keys())]
