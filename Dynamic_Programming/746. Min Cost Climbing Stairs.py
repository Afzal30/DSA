class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        memo = {}
        def helper(n):
            if n==len(cost):
                return 0

            if n in memo:
                return memo[n]
            
            if n<=len(cost)-2:
                memo[n] =  min(cost[n]+helper(n+1),cost[n]+helper(n+2))
                return memo[n]

            else:
                memo[n] =  cost[n]+helper(n+1)
                return memo[n]

        return min(helper(0),helper(1))


##efficent version of the above code

class Solution:

    def minCostClimbingStairs(self, cost):

        memo = {}

        def helper(n):

            if n >= len(cost):
                return 0

            if n in memo:
                return memo[n]

            memo[n] = cost[n] + min(helper(n+1), helper(n+2))

            return memo[n]

        return min(helper(0), helper(1))


#Tabulation Version (Bottom Up DP)

class Solution:

    def minCostClimbingStairs(self, cost):

        n = len(cost)

        dp = [0] * (n + 1)

        for i in range(2, n + 1):

            dp[i] = min(
                dp[i-1] + cost[i-1],
                dp[i-2] + cost[i-2]
            )

        return dp[n]


#Space Optimized version

class Solution:

    def minCostClimbingStairs(self, cost):

        prev2 = 0
        prev1 = 0

        for i in range(2, len(cost)+1):

            curr = min(
                prev1 + cost[i-1],
                prev2 + cost[i-2]
            )

            prev2 = prev1
            prev1 = curr

        return prev1
