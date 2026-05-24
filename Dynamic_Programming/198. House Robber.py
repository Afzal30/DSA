class Solution:
    def rob(self, nums: List[int]) -> int:


        @cache
        def helper(n,flag):
            if n>=len(nums):
                return 0

            if flag:
                return max( nums[n]+helper(n+1,False), helper(n+1,True))
            else:
                return helper(n+1,True)

        return max(helper(0,True),helper(0,False))

            
        
