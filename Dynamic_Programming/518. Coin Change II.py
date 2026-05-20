class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)
        @cache
        def helper(n,w):
            if n==0:
                return 0
            if w==0:
                return 1

            if coins[n-1]<=w:
                return helper(n,w-coins[n-1]) + helper(n-1,w)
            else:
                return helper(n-1,w)

        return helper(n,amount)
        
