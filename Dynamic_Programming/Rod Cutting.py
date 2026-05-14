# https://www.geeksforgeeks.org/dsa/cutting-a-rod-dp-13/


class Solution:
    def cutRod(self, price):
        #code here
        #w=sum(price)
        w= len(price)
        size = [x+1 for x in range(w) ]
        
        dp = [[0 for _ in range(w+1)] for _ in range(w+1)]
        
        print(dp)
        
        for i in range(1,w+1):
            for j in range(1,w+1):
                if size[i-1]<=j:
                    dp[i][j] = max(price[i-1]+dp[i][j-size[i-1]] , dp[i-1][j])
                    
                else:
                    dp[i][j] = dp[i-1][j]
                    
        return dp[8][8]
                    
                    
                    
                    
        
        
price = [1, 5, 8, 9, 10, 17, 17, 20]    

price = [3, 5, 8, 9, 10, 17, 17, 20]
obj = Solution()

print(obj.cutRod(price))
