class Solution:
    def maxProduct(self, n: int) -> int:
        a = float('-inf')
        b = float('-inf')
        for ele in str(n):
            if int(ele) > a :
                b=a
                a  = int(ele)
            elif int(ele) > b:
                b = int(ele)
        return a*b

        

        
