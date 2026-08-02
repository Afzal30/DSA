class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True

"""
This is a special case of 486. Predict the Winner.
Now, this problem introduces two important constraints:

The length of the piles is always even.
The total number of stones is odd, so a tie is impossible.
Intuition
We partition the piles into two groups according to their indices:

Pink : Even index
Blue : Odd index
Screenshot 2026-08-022 085944.png

Since both players play optimally, we can determine our strategy before the game begins:

Alice moves first, so the two ends of the array always have opposite parity.
Hence, on the first move, Alice always choose to either the Pink, or the Blue piles (whichever has the larger sum).
Observation:
During Alice's turn:

The two ends always have opposite parity.
During Bob's turn:

The two ends always have the same parity.
Screenshot 2026-08-02 124110.png

Therefore:

Alice always obtains the parity with the larger total sum, while
Bob obtains the parity with the smaller total sum.
Since the total number of stones is odd, the two parity sums cannot be equal.

Hence, Alice is guaranteed to collect more stones than Bob, so the answer is always

return true
​
 
​
 
Time Complexity: O(1)
Space Complexity: O(1)
"""
