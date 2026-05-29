class Solution:
    def minElement(self, nums: List[int]) -> int:
        def sumofdigits(n):
            n=str(n)
            tot = 0
            for ele in n:
                tot += int(ele)

            return tot
        mini = float('inf')
        for ele  in nums:
            mini = min(mini,sumofdigits(ele))
        return mini

#effective mathemetical logic 

"""
Observation
If we tabulate digit sums of n, an interesting pattern emerges:

Initially, values increase from 1–9, then reset every 10s, while also shifting upward by 1.
The same behavior repeats every 100s, every 1000s, and more generally at every power of 10.
This creates a layered, recursive structure driven by carry propagation at each digit position.
For the given constraints, the maximum possible digit sum occurs at:

9999=9+9+9+9= 
36
​
 
​
"""

class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = 36
        for n in nums:
            res = min(res, n - 9 * ((n//10) + (n//100) + (n//1000) + (n//10000)))
            
        return res
