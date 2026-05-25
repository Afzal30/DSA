#https://www.geeksforgeeks.org/problems/longest-common-substring1452/1

class Solution:
    def longCommSubstr(self, s1, s2):
        # code here
        n = len(s1)
        m = len(s2)
        
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        res = 0
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    
                    res = max(res,dp[i][j])
                    
                #else: 
                    #dp[i][j] = 0 #while inilizing we are making all cell a zero, option we can have else for understandnng the logic in future
                    
        return res


#recursive version

class Solution:
    def longCommSubstr(self, s1, s2):
        
        n = len(s1)
        m = len(s2)
        
        self.res = 0
        
        def helper(i, j, count):
            
            # base case
            if i == 0 or j == 0:
                self.res = max(self.res, count)
                return
            
            # choice diagram
            if s1[i-1] == s2[j-1]:
                helper(i-1, j-1, count + 1)
            else:
                self.res = max(self.res, count)
            
            # move independently like LCS
            helper(i-1, j, 0)
            helper(i, j-1, 0)
        
        helper(n, m, 0)
        
        return self.res
