class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        prev = '0'
        cur = ''
        if n==1 and k==1:
            return prev
        def invert(s):
            ans = ""
            for ele in s:
                if ele == "1":
                    ans += "0"
                else:
                    ans+="1"
            return ans

        
        for i in range(n-1):
            x = invert(prev)
            x = x[::-1]
            cur = prev + "1" + x
            prev = cur

        return cur[k-1]


        
