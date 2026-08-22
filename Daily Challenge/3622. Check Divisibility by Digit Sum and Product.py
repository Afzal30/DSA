class Solution:
    def checkDivisibility(self, n: int) -> bool:
        a = 0
        b = 1
        num = n
        while (num>0):
            rem = num%10
            
            a += rem
            b *= rem
            num //= 10

        return n%(a+b)==0

        
