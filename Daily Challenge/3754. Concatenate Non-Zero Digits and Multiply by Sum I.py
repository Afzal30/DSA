class Solution:
    def sumAndMultiply(self, n: int) -> int:
        n = str(n)
        digit = ""
        add = 0
        for ele in n:
            if ele != '0':
                digit += ele
            add += int(ele)
        return int(digit) * add if digit else 0

        
