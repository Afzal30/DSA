class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        seen = {}
        mn_diff = float('inf')
        for i, val in enumerate(nums):
            if val in seen:
                mn_diff = min(mn_diff, i - seen[val])
            seen[int(str(val)[::-1])] = i
        return mn_diff if mn_diff != float('inf') else -1
