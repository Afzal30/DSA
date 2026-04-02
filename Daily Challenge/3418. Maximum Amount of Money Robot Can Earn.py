class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m = len(coins)
        n = len(coins[0])
        
        # dp[i][j][k]
        dp = [[[float('-inf')] * 3 for _ in range(n)] for _ in range(m)]

        # Base case for (0,0)
        for k in range(3):
            if coins[0][0] >= 0:
                dp[0][0][k] = coins[0][0]
            else:
                dp[0][0][k] = 0 if k > 0 else coins[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                for k in range(3):
                    best_prev = float('-inf')

                    if i > 0:
                        best_prev = max(best_prev, dp[i-1][j][k])
                    if j > 0:
                        best_prev = max(best_prev, dp[i][j-1][k])

                    val = coins[i][j]

                    if val >= 0:
                        dp[i][j][k] = best_prev + val
                    else:
                        # do not neutralize
                        no_neutral = best_prev + val

                        # use neutralization if available
                        use_neutral = float('-inf')
                        if k > 0:
                            best_prev2 = float('-inf')
                            if i > 0:
                                best_prev2 = max(best_prev2, dp[i-1][j][k-1])
                            if j > 0:
                                best_prev2 = max(best_prev2, dp[i][j-1][k-1])
                            use_neutral = best_prev2

                        dp[i][j][k] = max(no_neutral, use_neutral)

        return max(dp[m-1][n-1][0], dp[m-1][n-1][1], dp[m-1][n-1][2])
