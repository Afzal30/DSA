class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def gcd(a,b):
            if b==0:
                return a
            else:
                return gcd(b, a%b)

        sum_even = 0
        sum_odd = 0
        
        for i in range(1,n*2+1):
            if i %2 ==0 :
                sum_even += i
            else:
                sum_odd += i
        #print(sum_odd,sum_even)
        return gcd(sum_odd,sum_even)
        

#another aproach

"""
The first n odd numbers sum to n * n
The First n even numbers sum to n * (n + 1)
gcd(n, n + 1) = 1, so the answer is n
"""

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n
