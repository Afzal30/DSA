class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        infi = float('inf')

        @cache
        def helper(n,w):

            #target amount achieved
            if w==0:
                return 0
            
            # no coins left
            if n==0:
                return infi

            if coins[n-1]<=w:
                return min(1 + helper(n,w-coins[n-1]), helper(n-1,w))
            else:
                return helper(n-1,w)

        res = helper(len(coins),amount)
        return res if res != infi else -1

        
