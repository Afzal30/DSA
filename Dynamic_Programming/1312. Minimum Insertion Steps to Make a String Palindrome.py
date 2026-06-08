#https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/description/
class Solution:
    def minInsertions(self, s: str) -> int:

        #code for longest common subsequence - find lcs
        n = len(s)
        rev_s = s[::-1]

        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i-1] == rev_s[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        lcs = dp[n][n]

        #the differen in the lenght of the string and lcs , is the number or insertion/deleition required to make a string palindrom
        return n - lcs        

"""
Intuition
To make a string palindrome, we want to keep as many characters as possible that are already helping form a palindrome.

A palindrome reads the same from left to right and right to left.

If we find the Longest Palindromic Subsequence (LPS), those characters can stay in their places. We only need to insert characters for the remaining ones.

So:

Minimum Insertions = Total Length of String − Longest Palindromic Subsequence
Now the question becomes: how do we find LPS?

A trick is:

Reverse the string.
Find the Longest Common Subsequence (LCS) between the original string and reversed string.
The LCS of these two strings is the Longest Palindromic Subsequence.
Example:

s = "mbadm"

Reverse:

"mdabm"

LCS = "mam" (length = 3)

String length = 5

Minimum insertions = 5 - 3 = 2

Approach
Create a copy of the string and reverse it.
Find the Longest Common Subsequence (LCS) between original string and reversed string.
The LCS length gives the Longest Palindromic Subsequence (LPS).
Subtract LPS length from original string length.
Return the answer.
To optimize space, instead of using a full 2D DP table, we only store the previous and current row.
"""
