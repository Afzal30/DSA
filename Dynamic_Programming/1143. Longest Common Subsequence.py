#https://leetcode.com/problems/longest-common-subsequence/

#recursion + memoization 

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n = len(text1)
        m = len(text2)

        hashmap = {}

        def lcs(n,m):

            if n==0 or m==0:
                return 0

            if (n,m) in  hashmap:
                return hashmap[(n,m)]

            if text1[n-1]==text2[m-1]:
                hashmap[(n,m)] = 1 + lcs(n-1,m-1)
                return hashmap[(n,m)]
            
            else:
                hashmap[(n,m)] =  max(lcs(n-1,m) , lcs(n,m-1))
                return hashmap[(n,m)]

        return lcs(n,m)


#bottom up or tabulization approach

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n = len(text1)
        m = len(text2)

        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        return dp[n][m]


        
        
