class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def dig_prod(n):
            prod = 1
            for ele in (str(n)):
                prod *= int(ele)
            return prod

        while True:
            prd =  dig_prod(n)
            if prd%t == 0:
                return n
            else:
                n+=1
        
