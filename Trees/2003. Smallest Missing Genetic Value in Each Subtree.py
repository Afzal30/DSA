#https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/description/

#https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/description/

class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(nums)
        self.tree = [ [] for _ in range(n)]
        self.visited = set()

        for i in range(1,n):
            p = parents[i]
            self.tree[p].append(i)

        ans = [1]*n

        one_idx = -1
        for i in range(n):
            if nums[i] == 1:
                one_idx = i
                break

        if one_idx == -1:
            return ans

        missing = 1
        cur,prev = one_idx,-1

        while cur != -1:
            for child in self.tree[cur]:
                if child == prev:
                    continue

                self.dfs(child,nums)


            self.visited.add(nums[cur])

            while missing in self.visited:
                missing += 1

            ans[cur] = missing

            prev,cur = cur, parents[cur]

        return ans

    def dfs(self,node,nums):
        self.visited.add(nums[node])
        for child in self.tree[node]:
            self.dfs(child,nums)
            

        
    
