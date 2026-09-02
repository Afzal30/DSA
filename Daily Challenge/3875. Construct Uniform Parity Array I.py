class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return True


"""
https://leetcode.com/problems/construct-uniform-parity-array-i/solutions/8494409/construct-uniform-parity-array-i-by-leet-25ko/?envType=daily-question&envId=2026-09-02
Intuition
This problem can be solved by simply analyzing the parity.

Let the length of the array nums 
1
​
  be n, and the task is to construct nums 
2
​
  such that all elements have the same parity (either all odd or all even).

Consider the following two cases:

nums 
1
​
  is all odd or all even: In this case, simply let nums 
2
​
 [i]=nums 
1
​
 [i] (i.e., use the first operation for all indices i), and the resulting nums 
2
​
  will be the same as the original array, naturally satisfying the condition.

nums 
1
​
  contains both odd and even numbers: Since even minus odd results in an odd number, we can arbitrarily choose an odd number x from nums 
1
​
  and then construct nums 
2
​
  as follows:

If nums 
1
​
 [i] is odd, then nums 
2
​
 [i]=nums 
1
​
 [i] (the first operation).

If nums 
1
​
 [i] is even, then nums 
2
​
 [i]=nums 
1
​
 [i]−x (the second operation, choosing j such that nums 
1
​
 [j]=x).

In this way, all elements in nums 
2
​
  will be odd, satisfying the requirements of the problem.

In summary, for any input that meets the conditions of the problem, we can always construct a valid nums 
2
​
 , so the answer is always true"""
