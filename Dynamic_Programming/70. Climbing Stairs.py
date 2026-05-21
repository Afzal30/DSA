class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n==0:
            return 1
        
        if n>=2:
            return self.climbStairs(n-1) + self.climbStairs(n-2)

        else:
            return self.climbStairs(n-1)
        
