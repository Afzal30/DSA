#solved own

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxi = max(nums)
        ans = 0
        for ele in nums:
            ans += (maxi-ele)
        return ans
        
