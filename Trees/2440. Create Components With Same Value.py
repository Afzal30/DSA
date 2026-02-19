#https://leetcode.com/problems/create-components-with-same-value/description/

class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        tree = [ [] for _ in nums]
        for u,v in edges:
            tree[u].append(v)
            tree[v].append(u)


        total = sum(nums)

        def helper(u,p,cand):
            ans = nums[u] + sum( [helper(v,u, cand) for v in tree[u] if v!=p ])

            return 0 if ans==cand else ans


        for k in range(len(nums),1,-1):

            if total%k == 0 and helper(0,-1,total//k)==0:
                return k-1

        return 0
