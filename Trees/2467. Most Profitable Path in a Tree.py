#https://leetcode.com/problems/most-profitable-path-in-a-tree/description/


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # ---------------------------
        # Phase 1: Bob's timing
        # ---------------------------
        bobTime = [inf] * n

        def dfs_bob(node, parent, time):
            if node == 0:
                bobTime[node] = time
                return True

            for nei in graph[node]:
                if nei != parent and dfs_bob(nei, node, time + 1):
                    bobTime[node] = time
                    return True

            return False

        dfs_bob(bob, -1, 0)

        # ---------------------------
        # Phase 2: Alice DFS
        # ---------------------------
        self.ans = -inf

        def dfs_alice(node, parent, time, profit):
            # Profit calculation
            if time < bobTime[node]:
                profit += amount[node]
            elif time == bobTime[node]:
                profit += amount[node] // 2

            # Check leaf
            is_leaf = True
            for nei in graph[node]:
                if nei != parent:
                    is_leaf = False
                    dfs_alice(nei, node, time + 1, profit)

            if is_leaf:
                self.ans = max(self.ans, profit)

        dfs_alice(0, -1, 0,  0)
        return self.ans
