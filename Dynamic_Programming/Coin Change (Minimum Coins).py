#https://www.geeksforgeeks.org/problems/number-of-coins1824/1

class Solution:
	def minCoins(self, coins, tot):
		# code here
		
		size = len(coins)
		
		dp = [[ float('inf') for _ in range(tot+1)] for _ in range(size+1)]
		
		for i in range(size+1):
		    dp[i][0] = 0
		    
		for i in range(1,size+1):
		     for j in range(1,tot+1):
		         if coins[i-1]<=j:
		             dp[i][j] = min( 1+dp[i][j-coins[i-1]], dp[i-1][j])
		         else:
		             dp[i][j] = dp[i-1][j]
		              
		return dp[size][tot] if not dp[size][tot]== float('inf') else -1
		    
		    
		   
		   
		  
		    
		    
