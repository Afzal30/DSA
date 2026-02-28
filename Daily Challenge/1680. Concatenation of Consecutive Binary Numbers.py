class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = ""
        for i in range(1,n+1):
            
            res += bin(i)[2:]

        ans = int(res,2)
        return ans % (10**9 + 7)
        
