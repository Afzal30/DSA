#https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/description/

class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        
        g = defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)

        ans = 0

        def dfs(node, parent):
            
            nonlocal ans

            max_with_leaf = price[node]
            max_without_leaf = 0

            for nei in g[node]:
                if nei == parent:
                    continue

                c, d = dfs(nei, node)

                ans = max(ans,
                          max_with_leaf + d,
                          max_without_leaf + c)

                max_with_leaf = max(max_with_leaf,
                                    price[node] + c)

                max_without_leaf = max(max_without_leaf,
                                       price[node] + d)

            return max_with_leaf, max_without_leaf

        dfs(0, -1)
        return ans
        
