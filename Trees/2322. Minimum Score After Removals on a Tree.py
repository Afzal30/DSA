#https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        graph = {}
        for u,v in edges:
            if u not in  graph:
                graph[u]=[v]
            else:
                graph[u].append(v)
            if v not in  graph:
                graph[v]=[u]
            else:
                graph[v].append(u)

        subtree_xor = [0] * n
        descendants = [ set() for _ in range(n)]

        def dfs(node,parent):
            subtree_xor[node] = nums[node]
            descendants[node].add(node)

            for neighbour in graph[node]:
                if neighbour != parent:
                    dfs(neighbour,node)
                    subtree_xor[node] ^= subtree_xor[neighbour]
                    descendants[node].update(descendants[neighbour])

        dfs(0,-1)

        print(graph,"---------",subtree_xor,"----------",descendants)

        total_xor = subtree_xor[0]
        min_score = float('inf')

        for i in range(1,n):
            for j in range(i+1,n):
                xor_i = subtree_xor[i]
                xor_j = subtree_xor[j]

                if j in descendants[i]:
                    val1 = xor_j
                    val2 = xor_i ^ xor_j
                    val3 = total_xor ^ xor_i

                elif i in descendants[j]:
                    val1 = xor_i
                    val2 = xor_i ^ xor_j
                    val3 = total_xor ^ xor_j

                else:
                    val1 = xor_i
                    val2 = xor_j
                    val3 = total_xor ^ xor_i ^ xor_j

                score = max(val1,val2,val3) - min(val1,val2,val3)
                min_score = min(min_score,score)

        return min_score



        
        
