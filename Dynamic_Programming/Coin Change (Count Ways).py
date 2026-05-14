#https://www.geeksforgeeks.org/problems/coin-change2448/1

class Solution:
    def count(self, coins, tot):
        # code here 
        
        dp = [[0 for _ in range(tot+1)] for _ in range(len(coins)+1)]
        
        for i in range(len(coins)+1):
            dp[i][0] = 1
            
        
        for i in range(1, len(coins) + 1):
            for j in range(1, tot+1):
                if coins[i-1] <= j:
                    dp[i][j] = dp[i][j-coins[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[len(coins)][tot]
