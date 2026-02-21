#own solution
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:

        def isprime(n):
            if n==1 or n==0:
                return False
            if n==2:
                return True
            for i in range(2,n//2+1):
                if n%i == 0 :
                    return False
            return True

        count = 0
        for i in range(left,right+1):
            bin_i = bin(i)[2:]
            bsum=0
            for ele in bin_i:
                bsum+=int(ele)
            if isprime(bsum):
                count+=1

        return count

        
#leetcode solution

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:

        return sum((1<<x.bit_count())&((1<<2)|(1<<3)|(1<<5)|(1<<7)|(1<<11)|(1<<13)|(1<<17)|(1<<19))>0 for x in range(left, right+1) )
