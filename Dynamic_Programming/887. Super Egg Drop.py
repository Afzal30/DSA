#https://leetcode.com/problems/super-egg-drop/description/

#dp - memoization - even after we will get time limit exceeded

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:

        memo = {}
        
        def solve(e,f):
            if f==0 or f==1:
                return f

            if e==1:
                return f

            if (e,f) in memo:
                return memo[(e,f)]

            mn = float('inf')

            for i in range(1,f+1):

                if (e-1,i-1) in memo:
                    broken =  memo[(e-1,i-1)]
                else:
                    broken = solve(e-1,i-1)
                    memo[(e-1,i-1)] = broken

                if (e,f-i) in memo:
                    not_broken =  memo[(e,f-i)]
                else:
                    not_broken = solve(e,f-i)
                    memo[(e,f-i)] = not_broken

                temp = 1 + max( broken , not_broken)
                mn = min(temp,mn)

            
            memo[(e,f)] = mn
            return mn

        return solve(k,n)



#using dp tabulization or bottom up approach

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:

        dp = [0] * (k + 1)
        moves = 0

        while dp[k] < n:
            moves += 1

            for eggs in range(k, 0, -1):
                dp[eggs] = dp[eggs] + dp[eggs - 1] + 1

        return moves

    
