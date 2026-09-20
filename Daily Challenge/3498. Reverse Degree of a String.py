class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        i=1
        for ele in s:
            val = 123-ord(ele)
            val *=i
            ans += val
            i+=1
        
        return ans
        
