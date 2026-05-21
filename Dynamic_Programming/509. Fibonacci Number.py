#https://leetcode.com/problems/fibonacci-number/


#basic recursion
class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        return self.fib(n-1) + self.fib(n-2)


#using cache - internal memoization
class Solution:
    @cache
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        return self.fib(n-1) + self.fib(n-2)


#explicit memoization using dictionary/hashmap
dp = {}

def fib(n):

    if n in dp:
        return dp[n]

    if n <= 1:
        return n

    dp[n] = fib(n-1) + fib(n-2)

    return dp[n]


#explicit memoization using set/hashset

class Solution:
    dp = [-1] * (n + 1)
    def fib(self, n: int) -> int:

        if n <= 1:
            return n

        if self.dp[n] != -1:
            return self.dp[n]

        self.dp[n] = self.solve(n-1) + self.solve(n-2)

        return self.dp[n]


#dp in iteration or tabulation or bottomup approach
class Solution:
    def fib(self, n: int) -> int:

        if n <= 1:
            return n

        dp = [0] * (n + 1)

        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

#same iteration , can be space optimized - Since only previous 2 values needed:
class Solution:
    def fib(self, n: int) -> int:

        if n <= 1:
            return n

        prev2 = 0
        prev1 = 1

        for i in range(2, n + 1):

            curr = prev1 + prev2

            prev2 = prev1
            prev1 = curr

        return prev1
